from bib_analise_lexica import AnaliseLexica
from bib_tratador_erro import TratadorErro
from estrutura_automato import EstruturaAutomato

automato = EstruturaAutomato()
analisador_lexico = AnaliseLexica()
tratador_de_erro = TratadorErro()
codigoFonte = open('../programaFonte.txt', 'r')
fila_lexico = analisador_lexico.lexico(codigoFonte)
codigoFonte.close()

stop = 1
fila_lexico.append(['$'])
t = 0
pilha = [0]
a = fila_lexico.pop(0)
token_anterior = a

while stop:
    s = pilha[len(pilha) - 1]
    dicionario_auxiliar = automato.tabela_action[s]

    if a[0] in dicionario_auxiliar.keys():
        lista = dicionario_auxiliar[a[0]]

        if lista[0] == 'S':
            t = lista[1]
            pilha.append(t)
            token_anterior = a
            a = fila_lexico.pop(0)
        elif lista[0] == 'R':
            regra = lista[1]
            roule = automato.gramatica_LLC[regra - 1]
            A = roule[0]
            beta = roule[2:]

            for i in range(0, len(beta)):
                pilha.pop()

            t = pilha[len(pilha) - 1]

            if t in automato.tabela_goto.keys():
                dicionario_auxiliar = automato.tabela_goto[t]

                if A in dicionario_auxiliar.keys():
                    pilha.append(dicionario_auxiliar[A])
                    print(' '.join(roule))
                    print()
        elif lista[0] == 'ACC':
            stop = 0
    else:
        if a[0] == 'Erro':
            print(a[1])
            a = fila_lexico.pop(0)
        else:
            valida_retorno_erro = tratador_de_erro.erro_insercao(a, s, token_anterior, fila_lexico)

            if len(valida_retorno_erro):
                a = valida_retorno_erro
            else:
                copia = fila_lexico.copy()
                quantAvancos = tratador_de_erro.erro_avanco(dicionario_auxiliar, copia, fila_lexico)

                if quantAvancos < len(fila_lexico):
                    print('Erro na linha {} coluna {}! Próximo ao token {}.\n'.format(a[1], a[2], a[0]))
                    fila_lexico = copia.copy()
                    a = fila_lexico.pop(0)
                else:
                    print('Erro na linha {} coluna {}, após o token {}.\n'.format(token_anterior[1], token_anterior[2],
                                                                                  token_anterior[0]))
                    stop = tratador_de_erro.erro_retorna(a, pilha)
