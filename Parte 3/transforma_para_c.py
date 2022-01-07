class TraduzParaC:
    def escrita_arquivo_c(self, lista_arq, lista_var):
        arquivo = open('traduzido.c', 'w')
        arquivo.write('#include<stdio.h>\n\n')
        arquivo.write('typedef enum { false, true } bool;\n')
        arquivo.write('typedef char literal[256];\n\n')
        arquivo.write('int main(){\n')

        espacos = [['    ']]

        # inserindo variaveis
        for i in lista_var:
            arquivo.write(''.join(espacos[0]))
            linha = ''.join(i)
            arquivo.write(linha + '\n')

        # inserindo resto do arquivo
        for i in range(0, len(lista_arq)):
            arquivo.write(''.join(espacos[len(espacos) - 1]))
            arquivo.write(lista_arq[i])

            if ('\n' not in lista_arq[i]):
                arquivo.write('\n')
            if ('if(' in lista_arq[i]):
                novo = espacos[len(espacos) - 1] * 2
                espacos.append(novo)
            if ((i + 1) < len(lista_arq) and '}' in lista_arq[i + 1] and len(espacos) > 1):
                espacos.pop()

        arquivo.write('}')
        arquivo.close()

    def criacao_temporaria(tipo, arquivo_c, arquivo_v, op1, op2, op):
        tamanho = len(arquivo_v)
        tx = 'T' + str(tamanho)  # Criando Tx
        arq = tx + ' = ' + op1[3] + ' ' + op[3] + ' ' + op2[3] + ';'  # Operação sendo realizada
        tx = [tipo, ' ', tx, ';']  # Declaração variável temporária
        arquivo_c.append(arq)  # Adicionando ao arquivo C
        arquivo_v.append(tx)  # Adicionando ao arquivo de declaração
