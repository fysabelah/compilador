from estrutura_automato import Estrutura_Automato


class Analise_Lexica:

    def verifica_tabela_simbolos(lexema, token, tipo):
        automato = Estrutura_Automato

        if (lexema not in automato.tabela_simbolos.keys()):
            aux = {lexema: [token, tipo]}
            automato.tabela_simbolos.update(aux)
            return token

        # Já está na tabela de símbolos. Pode ser palavra reservada ou id
        aux = automato.tabela_simbolos[lexema]
        return aux[0]

    def estado_aceito(lexema, estado, linha_error, coluna_error, fila):
        automato = Estrutura_Automato

        for chave in automato.aceitacao_automato.keys():
            if (estado in automato.aceitacao_automato[chave]):
                if (estado == 19):
                    aux = [chave, linha_error, coluna_error]
                    fila.append(aux)
                elif (estado == 21):
                    aux = [chave, linha_error, coluna_error]
                    fila.append(aux)
                else:
                    if (chave == 'id'):
                        fila.append(Analise_Lexica.verifica_tabela_simbolos(lexema, chave, '-'), linha_error,
                                    coluna_error)
                    else:
                        if (chave == "ab_p" or chave == "fc_p" or chave == "pt_v"):
                            aux = [lexema, linha_error, coluna_error]
                            fila.append(aux)
                        else:
                            aux = [chave, linha_error, coluna_error]
                            fila.append(aux)

                return

        frase_erro = 'Erro na linha ' + str(linha_error) + ' coluna ' + str(
            coluna_error) + '. A estrutura identificada ' + lexema + ' não pertence a linguagem.\n'
        aux = ['Erro', frase_erro]
        fila.append(aux)

    def presente_no_automato(caracter, estado):
        automato = Estrutura_Automato

        dicionario_auxiliar = automato.estados_automatos[estado]

        for chave in dicionario_auxiliar.keys():
            if caracter in chave:
                return (dicionario_auxiliar[chave])  # Proximo estado

        return (-1)  # Não presente no automato

    def verifica_contante_literal(palavra, interador, linha_error, fila):
        lex = ''

        while (interador < len(palavra) and palavra[interador] != '"'):
            lex += palavra[interador]
            interador += 1

        if (interador < len(palavra)): # encontrou o fechar de aspas
            aux = ['literal', linha_error, interador]
            fila.append(aux)
            return (interador + 1)

        # saiu do while por erro
        frase_erro = 'Erro na linha ' + str(linha_error) + ' coluna ' + str(
            interador) + '. Não foi identificado fechamento de ".\n'
        aux = ['Erro', frase_erro]
        fila.append(aux)

        return (interador)

    def ignorar_comentarios(palavra, interador, linha_error, fila):
        lex = ''

        while (interador < len(palavra) and palavra[interador] != '}'):
            lex += palavra[interador]
            interador += 1

        if (interador < len(palavra)):
            aux = ['comentario', linha_error, interador]
            fila.append(aux)

            return (interador + 1)

        # saiu do while por erro
        frase_erro = 'Erro na linha ' + str(linha_error) + ' coluna ' + str(
            interador) + '. Não foi identificado fechamento de }.\n'
        aux = ['Erro', frase_erro]
        fila.append(aux)

        return (interador)