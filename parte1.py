from typing import ChainMap


estados_automatos = {
  0: {';': 1, '(': 2, ')': 3, '+': 4, '-': 5, '*': 6, '/': 7, '=': 8, '>': 9, '<': 11, "EOF": 15, "abcdefghijklmnopqrstuvwxyzABCDEFGIJKLMNOPQRSTUVWXYZ": 16, "0123456789": 19, '{': 25, '"': 27, ' ': 0},
  9:  {'=': 10},
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

#------------Funções-------------#
def verificarTabelaSimbolos(lexema, token, tipo):
  if(lexema not in tabela_simbolos.keys()):
    if(token == 'id'):
      aux = {lexema: [token, tipo]}
      tabela_simbolos.update(aux)


def estadoAceito(lexema, estado, linhaerror):
  for chave in aceitacao_automato.keys():
    if(estado in aceitacao_automato[chave]):
      if(estado == 19):
        print('{} {} inteiro'.format(lexema, chave))
        verificarTabelaSimbolos(lexema, chave, 'inteiro')
        return
      elif(estado == 21):
        print('{} {} real'.format(lexema, chave))
        verificarTabelaSimbolos(lexema, chave, 'real')
        return
      else:
        verificarTabelaSimbolos(lexema, chave, '-')
        print('{} {} -'.format(lexema, chave))
        return

  print('Erro na linha {}. A estrutura identificada {} não pertence a linguagem.'.format(linhaerror, lexema))


def inAutomato(caracter, estado):
  auxDict = estados_automatos[estado]

  for chave in auxDict.keys():
    if caracter in chave:
      return(auxDict[chave]) #Proximo estado

  return(-1) #Não presente no automato
  

def verificarContanteLiteral(palavra, interador, linhaerror):
  lex = ''

  while(interador < len(palavra) and palavra[interador] != '"'):
    lex += palavra[interador]
    interador += 1
  
  if(interador < len(palavra)):
    #quer dizer que achou o fecha aspas
    print('{} literal -'.format(lex))
    return(interador + 1)
  else:
    #Saiu do while por erro, então printar o erro
    print('Erro na linha {}. Não foi identificador fechamento de ".'.format(linhaerror))
    return(interador)


def ignorarComentarios(palavra, interador, linhaerror):
  lex = ''
  while(interador < len(palavra) and palavra[interador] != '}'):
    lex += palavra[interador]
    interador += 1
    #Como é só para ignorar, não vou registrar
  
  if(interador > len(palavra)):
    #Saiu do while por erro, então printar o erro
    print('Erro na linha {}. Não foi identificador fechamento de }.'.format(linhaerror))
    return(interador)

  print('{} comentario -'.format(lex))
  return(interador + 1)

def lexico():
  contLinha = 0 #Conta a linha que está para informar o erro
  codigoFonte = open('programaFonte.txt', 'r')
  
  for linha in codigoFonte:
    contLinha += 1

    linha = linha.rstrip()
    linha = linha.lstrip()

    i = 0
    estado = 0
    flag = 0
    lexema = ''
  
    while(i < len(linha)):
      if(linha[i] == '"'):
          i+=1
          i = verificarContanteLiteral(linha, i, contLinha)
      elif(linha[i] == '{'):
        i+=1
        i = verificarContanteLiteral(linha, i, contLinha)
      else:
        flag = inAutomato(linha[i], estado)

        if(flag == -1 and estado == 0):
          print('Erro na linha {}. O {} não foi reconhecido pela linguagem.'.format(contLinha, linha[i]))
          i+=1
          flag = 0
        elif(estado == 0 and flag == 0): #Tira os espaços
          i += 1
        elif(flag == -1 and estado != 0):
          #verifica aceitação
          estadoAceito(lexema, estado, contLinha)
          estado = 0 #Para verificar se acha do começo
          lexema = ''
        elif(flag == 2 or flag == 3 or flag == 1 or flag == 4 or flag == 5 or flag == 6 or flag == 7 or flag == 8 or flag == 10 or flag == 12 or flag == 13 or flag == 14):#Estado de aceitação final, sem loop
            lexema+= linha[i]
            estadoAceito(lexema, flag, contLinha)
            estado = 0
            i+=1
            lexema = ''
        else:
          lexema += linha[i]
          i+=1
          estado = flag

    #Pode ocorrer de ser uma unica palavra
    if(len(lexema)):
      estadoAceito(lexema, estado, contLinha)
      
  #Adicionar EOF do final do arquivo
  print('EOF')
  codigoFonte.close()


#Main
lexico()