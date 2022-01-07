from estrutura_automato import EstruturaAutomato


class TratadorErro:

    def __init__(self):
        self.automo = EstruturaAutomato()

    def erro_retorna(self, a, pilha):
        if len(pilha) > 1:  # Retira onde o erro ocorreu
            pilha.pop()

            # Testar possibilidade de avanço
            s = pilha[len(pilha) - 1]
            aux = self.automo.tabela_action[s]

            while len(pilha) > 1 and a[0] not in aux.keys():
                pilha.pop()
                s = pilha[len(pilha) - 1]
                aux = self.automo.tabela_action[s]

            if len(pilha == 1):
                return 0

            return 1

        return 0  # Programa para e informa o erro. O estado atual é o estado de erro.

    def erro_avanco(self, dicionario, copia, fila_lexico):
        cont = 0

        for i in fila_lexico:
            if i[0] in dicionario.keys():
                return cont

            cont += 1
            copia.pop(0)

        return cont

    def erro_insercao(self, a, s, token_anterior, fila_lexico):
        if s == 0 and a[0] != 'inicio':
            fila_lexico.insert(0, a)
            print('Erro na linha 1 coluna 0, NÃO foi identificado a palavra reservada inicio.\n')

            return ['inicio', 1, 0]
        if s == 2 and a[0] != 'varinicio':
            fila_lexico.insert(0, a)
            print('Erro na linha 2 coluna 0, NÃO foi identificado a palavra reservada varinicio.\n')

            return ['varinicio', 1, 0]
        if s == 58 and a[0] != 'varfim':
            fila_lexico.insert(0, a)
            print('Erro na linha {} coluna {}, NÃO foi identificado a palavra reservada varfim.\n'.format(a[1], a[2]))

            return ['varfim', 1, 0]
        if a[0] == '$':
            print('Erro na linha {} coluna {}, após o token {}. NÃO foi identificado a palavra reservada fim.\n'.format(
                token_anterior[1], token_anterior[2], token_anterior[0]))
            fila_lexico.insert(0, a)

            return ['fim', token_anterior[1], 0]

        return []
