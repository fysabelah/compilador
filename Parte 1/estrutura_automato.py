class Estrutura_Automato:
    estados_automatos = {
        0: {';': 1, '(': 2, ')': 3, '+': 4, '-': 5, '*': 6, '/': 7, '=': 8, '>': 9, '<': 11, "EOF": 15,
            "abcdefghijklmnopqrstuvwxyzABCDEFGIJKLMNOPQRSTUVWXYZ": 16, "0123456789": 19, '{': 25, '"': 27, ' ': 0},
        9: {'=': 10},
        11: {'-': 12, '=': 8, '>': 14},
        16: {"abcdefghijklmnopqrstuvwxyzABCDEFGIJKLMNOPQRSTUVWXYZ": 16, "0123456789": 17, '_': 18},
        17: {"abcdefghijklmnopqrstuvwxyzABCDEFGIJKLMNOPQRSTUVWXYZ": 16, "0123456789": 17, '_': 18},
        18: {"abcdefghijklmnopqrstuvwxyzABCDEFGIJKLMNOPQRSTUVWXYZ": 16, "0123456789": 17, '_': 18},
        19: {"0123456789": 19, '.': 20, "eE": 22},
        20: {"0123456789": 21},
        21: {"0123456789": 21, 'eE': 22},
        22: {'+-': 23, "0123456789": 24},
        23: {"0123456789": 24},
        24: {"0123456789": 24},
        25: {"tudo": 25, '}': 26},
        27: {"tudo": 27, '"': 28}
    }

    aceitacao_automato = {
        "num": [19, 21, 24],
        "literal": [28],
        "id": [16, 17, 18],
        "comentario": [26],
        "eof": [15],
        "opr": [9, 11, 10, 13, 8, 14],
        "rcb": [12],
        "opm": [4, 5, 6, 7],
        "ab_p": [2],
        "fc_p": [3],
        "pt_v": [1]
    }

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
