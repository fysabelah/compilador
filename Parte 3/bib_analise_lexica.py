from estrutura_automato import EstruturaAutomato


class AnaliseLexica:

    def __init__(self):
        self.fila_lexico = []
        self.cont_linhas_arquivo = 0
        self.lexico_tem_erro = False

    def verifica_tabela_simbolos(self, lexema, token, tipo):
        automato = EstruturaAutomato()

        if lexema not in automato.tabela_simbolos.keys():
            aux = {lexema: [token, tipo]}
            automato.tabela_simbolos.update(aux)
            return token

        # Já está na tabela de símbolos. Pode ser palavra reservada ou id
        aux = automato.tabela_simbolos[lexema]
        return aux[0]

    def estado_aceito(self, lexema, estado, linha_error, coluna_error):
        automato = EstruturaAutomato()

        for chave in automato.aceitacao_automato.keys():
            if estado in automato.aceitacao_automato[chave]:
                if estado == 19:
                    aux = [chave, linha_error, coluna_error]
                    self.fila_lexico.append(aux)
                elif estado == 21:
                    aux = [chave, linha_error, coluna_error]
                    self.fila_lexico.append(aux)
                else:
                    if chave == 'id':
                        self.fila_lexico.append([self.verifica_tabela_simbolos(lexema, chave, '-'), linha_error,
                                                 coluna_error])
                    else:
                        if chave == "ab_p" or chave == "fc_p" or chave == "pt_v":
                            aux = [lexema, linha_error, coluna_error]
                            self.fila_lexico.append(aux)
                        else:
                            aux = [chave, linha_error, coluna_error]
                            self.fila_lexico.append(aux)

                return

        frase_erro = 'Erro na linha ' + str(linha_error) + ' coluna ' + str(
            coluna_error) + '. A estrutura identificada ' + lexema + ' não pertence a linguagem.\n'
        self.lexico_tem_erro = True
        print(frase_erro)

    def presente_no_automato(self, caracter, estado):
        automato = EstruturaAutomato()

        dicionario_auxiliar = automato.estados_automatos[estado]

        for chave in dicionario_auxiliar.keys():
            if caracter in chave:
                return dicionario_auxiliar[chave]  # Proximo estado

        return -1  # Não presente no automato

    def verifica_contante_literal(self, palavra, interador, linha_error):
        lex = ''

        while interador < len(palavra) and palavra[interador] != '"':
            lex += palavra[interador]
            interador += 1

        if interador < len(palavra):
            # quer dizer que achou o fecha aspas
            aux = ['literal', linha_error, interador]
            self.fila_lexico.append(aux)
            return interador + 1

        # Saiu do while por erro
        fraseErro = 'Erro na linha ' + str(linha_error) + ' coluna ' + str(
            interador) + '. Não foi identificado fechamento de ".\n'
        self.lexico_tem_erro = True
        print(fraseErro)

        return interador

    def ignorar_comentarios(self, palavra, interador, linha_error):
        lex = ''

        while interador < len(palavra) and palavra[interador] != '}':
            lex += palavra[interador]
            interador += 1

        if interador < len(palavra):
            aux = ['comentario', linha_error, interador]
            self.fila_lexico.append(aux)

            return interador + 1

        # saiu do while por erro
        frase_erro = 'Erro na linha ' + str(linha_error) + ' coluna ' + str(
            interador) + '. Não foi identificado fechamento de }.\n'
        self.lexico_tem_erro = True
        print(frase_erro)

        return interador

    def lexico(self, arquivo_codigo_fonte):
        automato = EstruturaAutomato()

        for linha in arquivo_codigo_fonte:
            self.cont_linhas_arquivo += 1
            cont_coluna_linha_arquivo = 0

            linha = linha.rstrip()
            linha = linha.lstrip()

            indice_caracter_linha = 0
            estado = 0
            flag = 0
            lexema = ''

            while indice_caracter_linha < len(linha):
                cont_coluna_linha_arquivo += 1

                if linha[indice_caracter_linha] == '"':
                    indice_caracter_linha += 1
                    indice_caracter_linha = self.verifica_contante_literal(linha, indice_caracter_linha,
                                                                           self.cont_linhas_arquivo)
                elif linha[indice_caracter_linha] == '{':
                    indice_caracter_linha += 1
                    indice_caracter_linha = self.ignorar_comentarios(linha, indice_caracter_linha,
                                                                     self.cont_linhas_arquivo)
                else:
                    flag = self.presente_no_automato(linha[indice_caracter_linha], estado)

                    if flag == -1 and estado == 0:
                        frase_erro = 'Erro na linha ' + str(self.cont_linhas_arquivo) + ' coluna ' + str(
                            indice_caracter_linha) + '. O ' + linha[
                                         indice_caracter_linha] + ' não foi reconhecido pela linguagem.\n'
                        self.lexico_tem_erro = True
                        print(frase_erro)

                        indice_caracter_linha += 1
                        flag = 0

                    elif estado == 0 and flag == 0:  # Tira os espaços
                        indice_caracter_linha += 1

                    elif flag == -1 and estado != 0:  # Verificar estado de aceitação
                        self.estado_aceito(lexema, estado, self.cont_linhas_arquivo, cont_coluna_linha_arquivo)

                        estado = 0  # Para verificar se acha do começo
                        lexema = ''

                    elif flag in automato.estado_aceitacao_sem_loop:
                        lexema += linha[indice_caracter_linha]
                        self.estado_aceito(lexema, flag, self.cont_linhas_arquivo, cont_coluna_linha_arquivo)
                        estado = 0
                        indice_caracter_linha += 1
                        lexema = ''

                    else:
                        lexema += linha[indice_caracter_linha]
                        indice_caracter_linha += 1
                        estado = flag
            if len(lexema):  # Verificação para o caso de palavra única
                self.estado_aceito(lexema, estado, self.cont_linhas_arquivo, cont_coluna_linha_arquivo)

        return self.fila_lexico
