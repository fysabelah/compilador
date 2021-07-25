from bib_analise_lexica import Analise_Lexica as analise_lexica

conta_linha_error = 0
arquivo_codigo_fonte = open('../programaFonte.txt', 'r')

for linha in arquivo_codigo_fonte:
    conta_linha_error += 1
    conta_coluna_error = 0

    linha = linha.rstrip()
    linha = linha.lstrip()

    indice_caracter_linha = 0
    estado = 0
    flag = 0
    lexema = ''

    while (indice_caracter_linha < len(linha)):
        conta_coluna_error += 1

        if (linha[indice_caracter_linha] == '"'):
            indice_caracter_linha += 1
            indice_caracter_linha = analise_lexica.verifica_contante_literal(linha, indice_caracter_linha,
                                                                             conta_linha_error)
        elif (linha[indice_caracter_linha] == '{'):
            indice_caracter_linha += 1
            indice_caracter_linha = analise_lexica.ignorar_comentarios(linha, indice_caracter_linha, conta_linha_error)
        else:
            flag = analise_lexica.presente_no_automato(linha[indice_caracter_linha], estado)

            if (flag == -1 and estado == 0):
                print('Erro na linha {} coluna {}. O {} não foi reconhecido pela linguagem.'.format(conta_linha_error,
                                                                                                    indice_caracter_linha,
                                                                                                    linha[
                                                                                                        indice_caracter_linha]))
                indice_caracter_linha += 1
                flag = 0
            elif (estado == 0 and flag == 0):  # Tira os espaços
                indice_caracter_linha += 1
            elif (flag == -1 and estado != 0):
                analise_lexica.estado_aceito(lexema, estado, conta_linha_error, conta_coluna_error)
                estado = 0  # Para verificar se acha do começo
                lexema = ''
            elif (
                    flag == 2 or flag == 3 or flag == 1 or flag == 4 or flag == 5 or flag == 6 or flag == 7 or flag == 8 or flag == 10 or flag == 12 or flag == 13 or flag == 14):  # Estado de aceitação final, sem loop
                lexema += linha[indice_caracter_linha]
                analise_lexica.estado_aceito(lexema, flag, conta_linha_error, conta_coluna_error)
                estado = 0
                indice_caracter_linha += 1
                lexema = ''
            else:
                lexema += linha[indice_caracter_linha]
                indice_caracter_linha += 1
                estado = flag

    # Pode ocorrer de ser uma unica palavra
    if (len(lexema)):
        analise_lexica.estado_aceito(lexema, estado, conta_linha_error, conta_coluna_error)

# Adicionar EOF do final do arquivo
print('EOF')
arquivo_codigo_fonte.close()
