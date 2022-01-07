from estrutura_automato import EstruturaAutomato


class AnaliseLexica:

    def verifica_tabela_simbolos(self, lexema, token, tipo):
        automato = EstruturaAutomato()

        if lexema not in automato.tabela_simbolos.keys():
            aux = {lexema: [token, tipo]}
            automato.tabela_simbolos.update(aux)
            print('{} {} {}'.format(lexema, token, tipo))
        else:
            # Já está na tabela de símbolos. Pode ser palavra reservada ou id
            aux = automato.tabela_simbolos[lexema]
            print("{} {} {}".format(lexema, aux[0], aux[1]))

    def estado_aceito(self, lexema, estado, linha_error, coluna_error):
        automato = EstruturaAutomato()

        for chave in automato.aceitacao_automato.keys():
            if estado in automato.aceitacao_automato[chave]:
                if estado == 19:
                    print('{} {} inteiro'.format(lexema, chave))
                elif estado == 21:
                    print('{} {} real'.format(lexema, chave))
                else:
                    if chave == 'id':
                        self.verifica_tabela_simbolos(lexema, chave, '-')
                    else:
                        print('{} {} {}'.format(lexema, chave, '-'))

                return

        print('Erro na linha {} coluna {}. A estrutura identificada {} não pertence a linguagem.'.format(linha_error,
                                                                                                         coluna_error,
                                                                                                         lexema))
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
            print('{} literal -'.format(lex))  # encontrou o fechar de aspas
            return interador + 1

        # saiu do while por erro
        print('Erro na linha {} coluna {}. Não foi identificador fechamento de ".'.format(linha_error, interador))
        return interador

    def ignorar_comentarios(self, palavra, interador, linha_error):
        lex = ''

        while interador < len(palavra) and palavra[interador] != '}':
            lex += palavra[interador]
            interador += 1

        if interador < len(palavra):
            print('{} comentario -'.format(lex))
            return interador + 1

        # saiu do while por erro
        print('Erro na linha {} e coluna {}. Não foi identificador fechamento de }}.'.format(linha_error, interador))
        return interador
