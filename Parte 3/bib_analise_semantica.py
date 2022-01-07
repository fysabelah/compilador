from estrutura_automato import EstruturaAutomato
from transforma_para_c import TraduzParaC


class AnaliseSemantica:
    def __init__(self):
        self.automato = EstruturaAutomato()
        self.traduzir_aquivo_txt_c = TraduzParaC()
        self.tem_erro_semantico = False

    def retorna_tipo(self, lexema):
        atributos = self.automato.tabela_simbolos[lexema]
        return atributos[1]

    def retorna_tipo_num(self, constante):
        if '.' in constante:
            return 'double'

        return 'int'

    def retorna_tipos_equivalentes(self, tipo1, tipo2):
        if tipo1 == tipo2:
            return 1
        return 0

    def verifica_equivalencia(self, tipo1, tipo2):
        if tipo1 == '-' or tipo2 == '-':
            self.tem_erro_semantico = True
            return 'erro_nao_declarada'

        flag = self.retorna_tipos_equivalentes(tipo1, tipo2)

        if flag:
            return tipo1  # Os tipos são equivalentes
        else:
            self.tem_erro_semantico = True
            return 'erro_tipo_diferente'

    def verifica_tipo(self, op1, op2):
        if op1[0] == 'num' and op2[0] == 'num':
            return self.verifica_equivalencia(self.retorna_tipo_num(op1[3]), self.retorna_tipo_num(op2[3]))
        elif op1[0] == 'id' and op2[0] == 'id':
            return self.verifica_equivalencia(self.retorna_tipo(op1[len(op1) - 1]),
                                              self.retorna_tipo(op1[len(op2) - 1]))
        else:
            if op1[0] == 'id':
                return self.verifica_equivalencia(self.retorna_tipo(op1[len(op1) - 1]), self.retorna_tipo_num(op2[3]))
            else:
                return self.verifica_equivalencia(self.retorna_tipo(op2[len(op2) - 1]), self.retorna_tipo_num(op1[3]))

    def regras_semanticas(self, regra, semantico, arquivo, vartx):
        if regra == 6:
            correcao_nome_tipo = ''
            var = semantico.pop()
            var = var[3]
            tipo = semantico.pop()

            # Atualizando tabela de símbolos
            if tipo[0] == 'lit':
                correcao_nome_tipo = 'literal'
                self.automato.tabela_simbolos[var] = ['id', correcao_nome_tipo]
            elif tipo[0] == 'inteiro':
                correcao_nome_tipo = 'int'
                self.automato.tabela_simbolos[var] = ['id', correcao_nome_tipo]
            elif tipo[0] == 'real':
                correcao_nome_tipo = 'double'
                self.automato.tabela_simbolos[var] = ['id', correcao_nome_tipo]

            aux = correcao_nome_tipo + ' ' + var + ';'
            arquivo.append(aux)
        elif regra == 5:
            for i in range(0, 3):
                arquivo.append('\n')
        elif regra == 12:
            # A forma de escreve do literal e num é a mesma. Muda apenas o id
            semantico.pop()  # escreva
            a_escrever = semantico.pop()

            if a_escrever[0] == 'id':
                tipo = self.retorna_tipo(a_escrever[3])

                if tipo == '-':
                    print('Erro na linha {}: Variável não declarada'.format(a_escrever[1]))
                    self.tem_erro_semantico = True
                else:
                    if tipo == 'int':
                        arquivo.append('printf("%d", ' + a_escrever[3] + ');')
                    elif tipo == 'double':
                        arquivo.append('printf("%lf", ' + a_escrever[3] + ');')
                    else:
                        arquivo.append('printf("%s", ' + a_escrever[3] + ');')
            else:
                arquivo.append('printf("' + a_escrever[3] + '");')
        elif regra == 11:
            semantico.pop()  # leia
            var = semantico.pop()
            tipo = self.retorna_tipo(var[len(var) - 1])

            if tipo == '-':
                print('Erro na linha {}: Variável não declarada'.format(var[1]))
                self.tem_erro_semantico = True
            else:
                if tipo == 'literal':
                    arquivo.append('scanf("%s", ' + var[len(var) - 1] + ');')
                elif tipo == 'int':
                    arquivo.append('scanf("%d", &' + var[len(var) - 1] + ');')
                else:
                    arquivo.append('scanf("%lf", &' + var[len(var) - 1] + ');')
        elif regra == 25:
            # Exclusivo para o se, por isso farei esse tipo de exclusão
            semantico.pop()  # se
            semantico.pop()  # (
            op1 = semantico.pop()  # id or num
            op2 = semantico.pop()  # simbolo
            op3 = semantico.pop()  # id or num
            semantico.pop()  # )

            # Retornar se a operação pode ou não ser realizada
            flag = self.verifica_tipo(op1, op3)
            if flag == 'erro_nao_declarada':
                print('Erro na linha {}: Variável não declarada'.format(op1[1]))
            elif flag == 'erro_tipo_diferente':
                print('Erro na linha {}: Operando com tipos incompatíveis'.format(op1[1]))
            else:
                tipo = 'bool'
                self.traduzir_aquivo_txt_c.criacao_temporaria(tipo, arquivo, vartx, op1, op3, op2)
        elif regra == 24:
            semantico.pop()  # retirar o então do se anterior
            var = vartx[len(vartx) - 1]  # vem sempre após o 24. Logo acabei de gerar a temporária
            se = 'if(' + var[2] + '){'
            arquivo.append(se)
        elif regra == 23:
            semantico.pop()  # retirar o fimse
            arquivo.append('}')
        elif regra == 18:
            # Aqui vou pegar o primeiro e não o último
            op1 = semantico.pop(0)  # 1
            operacao = semantico.pop(0)  # +
            op2 = semantico.pop(0)  # B

            tipo = self.verifica_tipo(op1, op2)
            if tipo == 'erro_nao_declarada':
                print('Erro na linha {}: Variável não declarada'.format(op1[1]))
            elif tipo == 'erro_tipo_diferente':
                print('Erro na linha {}: Operando com tipos incompatíveis'.format(op1[1]))
            elif tipo != 'literal':
                self.traduzir_aquivo_txt_c.criacao_temporaria(tipo, arquivo, vartx, op2, op1, operacao)
                var = vartx[len(vartx) - 1]
                semantico.insert(0, [var[0], op2[1], op2[2], var[2]])  # Inserção será utilizado na Regra 17
        elif regra == 17:
            # Essa regra trata-se obrigatoriamente de um id na hora de verificar tipos
            id = semantico.pop()
            semantico.pop()
            op = semantico.pop()

            tipo = self.retorna_tipo(id[3])
            flag = 0
            if tipo == '-':
                print('Erro na linha {}: Variável não declarada'.format(id[1]))
                self.tem_erro_semantico = True
            else:
                # Analisando os tipos
                if 'T' in op[3]:
                    flag = self.retorna_tipos_equivalentes(tipo, op[0])
                elif op[0] == 'num':
                    flag = self.retorna_tipos_equivalentes(self.retorna_tipo_num(op[3]), tipo)
                else:
                    # op também é id
                    flag = self.retorna_tipos_equivalentes(self.retorna_tipo(op[3]), tipo)

                # Verificando compatibilidade
                if flag:
                    arquivo.append(id[3] + ' = ' + op[3] + ';')
                else:
                    print('Erro na linha {}: Tipos diferentes para atribuição'.format(id[1]))
                    self.tem_erro_semantico = True
