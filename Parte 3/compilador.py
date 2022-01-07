from bib_analise_lexica import AnaliseLexica
from bib_tratador_erro import TratadorErro
from estrutura_automato import EstruturaAutomato
from bib_analise_semantica import AnaliseSemantica
from transforma_para_c import TraduzParaC

automato = EstruturaAutomato()
analisador_lexico = AnaliseLexica()
tratador_de_erro = TratadorErro()
analisador_semantico = AnaliseSemantica()
traduzir_para_c = TraduzParaC()

codigoFonte = open('../programaFonte.txt', 'r')
fila_lexico = analisador_lexico.lexico(codigoFonte)
codigoFonte.close()
sintatico_tem_erro = False

stop = 1
t = 0
pilha = [0]
fila_lexico.append(['$'])
a = fila_lexico.pop(0)
token_anterior = a

semantico = []
arquivoC = []
arquivoTx = []


def sem_erro_lexico_sintatico():
    return not analisador_lexico.lexico_tem_erro and not sintatico_tem_erro


def sem_erro_lexico_sintatico_semantico():
    return not analisador_lexico.lexico_tem_erro and not sintatico_tem_erro and not analisador_semantico.tem_erro_semantico


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

            if (a[0] != 'inicio' and a[0] != 'varinicio' and a[0] != 'varfim' and a[0] != ';' and a[0] != 'fim' and a
            [0] != '$'):
                semantico.insert(0, a)

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

                    if len(semantico) > 0 and sem_erro_lexico_sintatico():
                        analisador_semantico.regras_semanticas(regra, semantico, arquivoC, arquivoTx)

        elif lista[0] == 'ACC' and sem_erro_lexico_sintatico_semantico():
            stop = 0
            traduzir_para_c.escrita_arquivo_c(arquivoC, arquivoTx)
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
