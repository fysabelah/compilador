#Esta compõe a primeira parte, que contempla tabela de símbolos e análise léxica
import string

'''Se parou e não é estado de aceitação, imprimir erro!'''
aceitacao_automato = { "num": [19, 21, 24],
                       "literal": 28,
					   "id": [16, 17, 18],
					   "comentario": 26,
					   "eof": 15,
					   "opr": [9, 11, 10, 13, 8, 14],
					   "rcb": 12,
					   "opm": [4, 5, 6, 7],
					   "ab_p": 2,
					   "fc_p": 3,
					   "pt_v": 1,
}

'''Descrita na estrutura: lexema, token, tipo'''
tabela_simbolos = {
  "inicio": ["inicio", "-"],
  "varinicio": ["varinicio", "-"],
  "varfim": ["varfim", "-"],
  "escreva": ["escreva", "-"],
  "leia": ["leia", "-"],
  "se": ["se", "-"],
  "entao": ["entao", "-"],
  "fimse": ["fimse", "-"],
  "fim": ["fim", "-"],
  "inteiro": ["inteiro", "-"],
  "lit": ["lit", "-"],
  "real": ["real", "-"]
}

estados_automatos = {
  0: {';': 1, '(': 2, ')': 3, '+': 4, '-': 5, '*': 6, '/': 7, '=': 8, '>': 9, '<': 11, "EOF": 15, "Aa-zZ": 16, "0-9": 19, '{': 25, '"': 27, "tabespn": 0},
  9:  {'=': 10},
  11: {'-': 12, '=': 8, '>': 14},
  16: {"Az-aZ": 16, "0-9": 17, '_': 18},
  17: {"Az-aZ": 16, "0-9": 17, '_': 18},
  18: {"Az-aZ": 16, "0-9": 17, '_': 18},
  19: {"0-9": 19, '.': 20, 'eE': 22},
  20: {"0-9": 21},
  21: {"0-9": 21, 'eE': 22},
  22: {'+-': 23, "0-9": 24},
  23: {"0-9": 24},
  24: {"0-9": 24},
  25: {"tudo": 25, '}': 26},
  27: {"tudo": 27, '"': 28}
}

'''Auxilar ao autômato!'''
alfabeto = list(string.ascii_letters)
notacao_cientifica = ['E', 'e']
digitos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''Comentário e constante literal podem ter de tudo. A diferença é que um começa e termina com {} e o outro com ""'''