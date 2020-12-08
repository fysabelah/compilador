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

#Esta estrutura (fila_lexico) é para corrigir a forma que o lexico() foi implementado. Verificando a parte dois do trabalho, verifiquei que sempre vai passar um token, porém para ;, ( e ) passa o próprio lexema.
fila_lexico = []

gramatica_LLC = [
  ["P'", "→", "P"],
  ["P", "→", "inicio", "V", "A"],
  ["V", "→", "varinicio", "LV"],
  ["LV", "→", "D", "LV"],
  ["LV", "→", "varfim", ";"],
  ["D", "→", "id", "TIPO", ";"],
  ["TIPO", "→", "inteiro"],
  ["TIPO", "→", "real"],
  ["TIPO", "→", "lit"],
  ["A", "→", "ES", "A"],
  ["ES", "→", "leia", "id", ";"],
  ["ES", "→", "escreva", "ARG", ";"],
  ["ARG", "→", "literal"],
  ["ARG", "→", "num"],
  ["ARG", "→", "id"],
  ["A", "→", "CMD", "A"],
  ["CMD", "→", "id", "rcb", "LD", ";"],
  ["LD", "→", "OPRD", "opm", "OPRD"],
  ["LD", "→", "OPRD"],
  ["OPRD", "→", "id"],
  ["OPRD", "→", "num"],
  ["A", "→", "COND",  "A"],
  ["COND", "→", "CABEÇALHO", "CORPO"],
  ["CABEÇALHO", "→", "se", "(", "EXP_R", ")", "entao"],
  ["EXP_R", "→", "OPRD", "opr", "OPRD"],
  ["CORPO", "→", "ES", "CORPO"],
  ["CORPO", "→", "CMD", "CORPO"],
  ["CORPO", "→", "COND", "CORPO"],
  ["CORPO", "→", "fimse"],
  ["A", "→", "fim"]
]

regras_semanticas = [
    ['-'],
    ['-'],
    ['-'],
    ['-'],
    ['imprime 3 linha brancas'],
    ['id.tipo <-TIPO.tipo', 'imprime(TIPO. tipo id.lexema;)'],
    ['TIPO.tipo <- inteiro.tipo'],
    ['TIPO.tipo <- real.tipo'],
    ['TIPO.tipo <- lit.tipo'],
    ['-'],
    ['verificar declarado'],
    ['imprime printf("ARG.lexema");'],
    ['ARG.atributos <- literal.atributos'],
    ['ARG.atributos <- num.atributos'],
    ['verificar declarado']
]

tabela_goto = {
    0:{'P': 1},
  2:{'V':3},
  3:{'A':5, 'ES':6, 'CMD':7, 'COND':8, 'CABEÇALHO':13},
  4:{'LV':15, 'D':16},
  6:{'A':55, 'ES':6, 'CMD':7, 'COND':8, 'CABEÇALHO':13},
  7:{'A':56, 'ES':6, 'CMD':7, 'COND':8, 'CABEÇALHO':13},
  8:{'A':57, 'ES':6, 'CMD':7, 'COND':8, 'CABEÇALHO':13},
  11:{'ARG':27},
  13:{'ES':48, 'CMD':49, 'COND':50,'CABEÇALHO':13, 'CORPO':47},
  16:{'LV':24, 'D':16},
  18:{'TIPO':19},
  32:{'OPRD':35,'EXP_R':36},
  39:{'OPRD':40},
  41:{'LD':42, 'OPRD':44},
  45:{'OPRD':46},
  48:{'ES':48, 'CMD':49,'COND':50,'CABEÇALHO':13, 'CORPO':52},
  49:{'ES':48, 'CMD':49,'COND':50,'CABEÇALHO':13, 'CORPO':53},
  50:{'ES':48, 'CMD':49,'COND':50,'CABEÇALHO':13, 'CORPO':54}
}

tabela_action = {
	0:{'inicio': ['S',2]},
  1:{'$':['ACC']},
  2:{'varinicio':['S',4]},
  3:{'id':['S',12], 'leia':['S',10], 'escreva':['S',11], 'se':['S',14], 'fim':['S',9]},
  4:{'varfim':['S',17], 'id':['S',18]},
  5:{'$':['R',2]},
  6:{'id':['S',12], 'leia':['S',10], 'escreva':['S',11], 'se':['S',14], 'fim':['S',9]},
  7:{'id':['S',12], 'leia':['S',10], 'escreva':['S',11], 'se':['S',14], 'fim':['S',9]},
  8:{'id':['S',12], 'leia':['S',10], 'escreva':['S',11], 'se':['S',14], 'fim':['S',9]},
  9:{'$':['R',30]},
  10:{'id':['S',25]},
  11:{'id':['S',30], 'literal':['S',28],'num':['S',29]},
  12:{'rcb':['S',41]},
  13:{'id':['S',12], 'leia':['S',10], 'escreva':['S',11], 'se':['S',14], 'fim':['S',51]},
  14:{'(':['S',32]},
  15:{'id':['R',3], 'leia':['R',3], 'escreva':['R',3], 'se':['R',3], 'fim':['R',3]},
  16:{'varfim':['S',17], 'id':['S',18]},
  17:{';':['S',23]},
  18:{'inteiro':['S',20], 'real':['S',21],'lit':['S',22]},
  19:{';':['S',58]},
  20:{';':['R',7]},
  21:{';':['R',8]},
  22:{';':['R',9]},
  23:{'id':['R',5], 'leia':['R',5], 'escreva':['R',5], 'se':['R',5], 'fim':['R',5]},
  24:{'id':['R',4], 'leia':['R',4], 'escreva':['R',4], 'se':['R',4], 'fim':['R',4]},
  25:{';':['S',26]},
  26:{'id':['R',11], 'leia':['R',11], 'escreva':['R',11], 'se':['R',11], 'fimse':['R',11], 'fim':['R',11]},
  27:{';':['S',31]},
  #'id':['R',14], 'leia':['R',14], 'escreva':['R',14], 'se':['R',14], 'fimse':['R',14], 'fim':['R',14]
  28:{';':['R',13]},
  29:{';':['R',14]},
  30:{';':['R',15]},
  31:{'id':['R',12], 'leia':['R',12], 'escreva':['R',12], 'se':['R',12], 'fimse':['R',12], 'fim':['R',12]},
  32:{'id':['S',33], 'num':['S',34]},
  33:{'opm':['R',20], ')':['R',20], 'opr':['R',20], ';':['R',20]},
  34:{'opm':['R',21], ')':['R',21], 'opr':['R',21], ';':['R',21]},
  35:{'opr':['S',39]},
  36:{')':['S',37]},
  37:{'entao':['S',38]},
  38:{'id':['R',24], 'leia':['R',24], 'escreva':['R',24], 'se':['R',24], 'fimse':['R',24]},
  39:{'id':['S',33], 'num':['S',34]},
  40:{')':['R',25]},
  41:{'id':['S',33], 'num':['S',34]},
  42:{';':['S',43]},
  43:{'id':['R',17], 'leia':['R',17], 'escreva':['R',17], 'se':['R',17], 'fimse':['R',17], 'fim':['R',17]},
  44:{'opm':['S',45], ';':['R',19]},
  45:{'id':['S',33], 'num':['S',34]},
  46:{';':['R',18]},
  47:{'id':['R',23], 'leia':['R',23], 'escreva':['R',23], 'se':['R',23], 'fimse':['R',23], 'fim':['R',23]},
  48:{'id':['S',12], 'leia':['S',10], 'escreva':['S',11], 'se':['S',14], 'fimse':['S',51]},
  49:{'id':['S',12], 'leia':['S',10], 'escreva':['S',11], 'se':['S',14], 'fimse':['S',51]},
  50:{'id':['S',12], 'leia':['S',10], 'escreva':['S',11], 'se':['S',14], 'fimse':['S',51]},
  51:{'id':['R',29], 'leia':['R',29], 'escreva':['R',29], 'se':['R',29], 'fimse':['R',29], 'fim':['R',29]},
  52:{'id':['R',26], 'leia':['R',26], 'escreva':['R',26], 'se':['R',26], 'fimse':['R',26], 'fim':['R',26]},
  53:{'id':['R',27], 'leia':['R',27], 'escreva':['R',27], 'se':['R',27], 'fimse':['R',27], 'fim':['R',27]},
  54:{'id':['R',28], 'leia':['R',28], 'escreva':['R',28], 'se':['R',28], 'fimse':['R',28], 'fim':['R',28]},
  55:{'$':['R',10]},
  56:{'$':['R',16]},
  57:{'$':['R',22]},
  58:{'varfim':['R', 6],'id':['R', 6]}
}

#--------------------------------------Funções--------------------------------------#
def verificarTabelaSimbolos(lexema, token, tipo, linha, coluna):
  if(lexema not in tabela_simbolos.keys()):
    aux = {lexema: [token, tipo]}
    tabela_simbolos.update(aux)
    #print('{} {} {}'.format(lexema, token, tipo))
    aux2 = [token, linha, coluna, lexema]
    fila_lexico.append(aux2)
  else:
    #Já está na tabela de símbolos. Pode ser palavra reservada ou id
    aux = tabela_simbolos[lexema]
    #print("{} {} {}".format(lexema, aux[0], aux[1]))
    aux2 = [aux[0], linha, coluna, lexema]
    fila_lexico.append(aux2)

def estadoAceito(lexema, estado, linhaerror, colunaerror):
  for chave in aceitacao_automato.keys():
    if(estado in aceitacao_automato[chave]):
      if(estado == 19):
        #print('{} {} inteiro'.format(lexema, chave))
        aux = [chave, linhaerror, colunaerror, lexema]
        fila_lexico.append(aux)
      elif(estado == 21):
        #print('{} {} real'.format(lexema, chave))
        aux = [chave, linhaerror, colunaerror, lexema]
        fila_lexico.append(aux)
      else:
        if(chave == 'id'):
          verificarTabelaSimbolos(lexema, chave, '-', linhaerror, colunaerror)
        else:
          #print('{} {} {}'.format(lexema, chave, '-'))

          if(chave == "ab_p" or chave == "fc_p" or chave == "pt_v"):
            aux = [lexema, linhaerror, colunaerror]
            fila_lexico.append(aux)
          else:
            aux = [chave, linhaerror, colunaerror, lexema]
            fila_lexico.append(aux)
      
      return

  print('Erro na linha {} coluna {}. A estrutura identificada {} não pertence a linguagem.'.format(linhaerror, colunaerror, lexema))

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
    #print('{} literal -'.format(lex))
    aux = ['literal', linhaerror, interador, lex]
    fila_lexico.append(aux)
    return(interador + 1)
  else:
    #Saiu do while por erro, então printar o erro
    print('Erro na linha {} coluna {}. Não foi identificador fechamento de ".'.format(linhaerror, interador))
    return(interador)

def ignorarComentarios(palavra, interador, linhaerror):
  lex = ''

  while(interador < len(palavra) and palavra[interador] != '}'):
    lex += palavra[interador]
    interador += 1
  
  if(interador < len(palavra)):
    #print('{} comentario -'.format(lex))
    aux = ['comentario', linhaerror, interador]
    fila_lexico.append(aux)
    return(interador + 1)

  #Saiu do while por erro, então printar o erro
  print('Erro na linha {} e coluna {}. Não foi identificador fechamento de }}.'.format(linhaerror, interador))
  return(interador)

def lexico():
  contLinha = 0 #Conta a linha que está para informar o erro
  codigoFonte = open('programaFonte.txt', 'r')
  
  for linha in codigoFonte:
    contLinha += 1
    contColuna = 0

    linha = linha.rstrip()
    linha = linha.lstrip()

    i = 0
    estado = 0
    flag = 0
    lexema = ''
  
    while(i < len(linha)):
      contColuna += 1 #Conta a coluna que está para informar o erro

      if(linha[i] == '"'):
          i+=1
          i = verificarContanteLiteral(linha, i, contLinha)
      elif(linha[i] == '{'):
        i+=1
        i = ignorarComentarios(linha, i, contLinha)
      else:
        flag = inAutomato(linha[i], estado)

        if(flag == -1 and estado == 0):
          print('Erro na linha {} coluna {}. O {} não foi reconhecido pela linguagem.'.format(contLinha, i, linha[i]))
          i+=1
          flag = 0
        elif(estado == 0 and flag == 0): #Tira os espaços
          i += 1
        elif(flag == -1 and estado != 0):
          #verifica aceitação
          estadoAceito(lexema, estado, contLinha, contColuna)
          estado = 0 #Para verificar se acha do começo
          lexema = ''
        elif(flag == 2 or flag == 3 or flag == 1 or flag == 4 or flag == 5 or flag == 6 or flag == 7 or flag == 8 or flag == 10 or flag == 12 or flag == 13 or flag == 14):#Estado de aceitação final, sem loop
            lexema+= linha[i]
            estadoAceito(lexema, flag, contLinha, contColuna)
            estado = 0
            i+=1
            lexema = ''
        else:
          lexema += linha[i]
          i+=1
          estado = flag

    #Pode ocorrer de ser uma unica palavra
    if(len(lexema)):
      estadoAceito(lexema, estado, contLinha, contColuna)
      
  #Adicionar EOF do final do arquivo
  #print('EOF')
  codigoFonte.close()

def tratamentoErrosRetorna(a, pilha):
  if(len(pilha) > 1):
    #retirada onde ocorreu o erro
    pilha.pop()
    
    #testar avanço
    s = pilha[len(pilha) - 1]
    aux = tabela_action[s]

    while(len(pilha) > 1 and a[0] not in aux.keys()):
      pilha.pop()
      s = pilha[len(pilha) - 1]
      aux = tabela_action[s]
    
    if(len(pilha) == 1):
      return(0)
    else:
      return(1)
  else:
    #Programa para e informa o erro e pronto, pois o estado que está é o erro e se tirá-lo sobre apenas o 0.
    return(0)

def tratamentoErrosAvanco(dicionario, copia):
  cont = 0

  for i in fila_lexico:
    if(i[0] in dicionario.keys()):
      return(cont)
    else:
      cont+=1
      copia.pop(0)
  
  return(cont)

def retornaTipo(lexema):
    atributos = tabela_simbolos[lexema]
    return(atributos[1])

def retornaTipoNum(constante):
    if('.' in constante):
        return('double')
    
    return('int')

def tiposEquivalentes(tipo1, tipo2):
    if(tipo1 == tipo2):
        return(1)
    return(0)

def verificaEquivalencia(tipo1, tipo2):
  if(tipo1 == '-' or tipo2 == '-'):
    return('erro1')#Retorna erro não declarada
  else:
    flag = tiposEquivalentes(tipo1, tipo2)

    if(flag):
      return(tipo1)#Os tipos são equivalentes
    else:
      return('erro2')#Retorna erro tipos são diferentes

def verificaTipo(op1, op2):
    if(op1[0] == 'num' and op2[0] == 'num'):
        return(verificaEquivalencia(retornaTipoNum(op1[3]), retornaTipoNum(op2[3])))
    elif(op1[0] == 'id' and op2[0] == 'id'):
        return(verificaEquivalencia(retornaTipo(op1[len(op1) - 1]), retornaTipo(op1[len(op2) - 1])))
    else:
        if(op1[0] == 'id'):
          return(verificaEquivalencia(retornaTipo(op1[len(op1) - 1]), retornaTipoNum(op2[3])))
        else:
          return(verificaEquivalencia(retornaTipo(op2[len(op2) - 1]), retornaTipoNum(op1[3])))

def escritaArquivoC(listaArq, listaVar):
    arquivo = open('traduzido.c', 'w')
    arquivo.write('#include<stdio.h>\n\n')
    arquivo.write('typedef enum { false, true } bool;\n')
    arquivo.write('typedef char literal[256];\n\n')
    arquivo.write('int main(){\n')

    espacos = [['    ']]

    #inserindo variaveis
    for i in listaVar:
        arquivo.write(''.join(espacos[0]))
        linha = ''.join(i)
        arquivo.write(linha + '\n')

    #inserindo resto do arquivo
    for i in range(0, len(listaArq)):
        arquivo.write(''.join(espacos[len(espacos) - 1]))
        arquivo.write(listaArq[i])
        
        if('\n' not in listaArq[i]):
            arquivo.write('\n')
        if('if(' in listaArq[i]):
            novo = espacos[len(espacos) - 1] * 2
            espacos.append(novo)
        if((i+1) < len(listaArq) and '}' in listaArq[i+1] and len(espacos) > 1):
            espacos.pop()
        
    arquivo.write('}')
    arquivo.close()

def regrasSemanticas(regra, semantico, arquivo, vartx):
    if(regra == 6):
        tipoF = ''
        var = semantico.pop()
        var = var[3]
        tipo = semantico.pop()
        
        #Atualizando tabela de símbolos
        if(tipo[0] == 'lit'):
            tipoF = 'literal'
            tabela_simbolos[var] = ['id', tipoF]
        elif(tipo[0] == 'inteiro'):
            tipoF = 'int'
            tabela_simbolos[var] = ['id', tipoF]
        elif(tipo[0] == 'real'):
            tipoF = 'double'
            tabela_simbolos[var] = ['id', tipoF]
        
        aux = tipoF + ' ' + var + ';'
        arquivo.append(aux)
    elif(regra == 5):
        for i in range(0,3):
            arquivo.append('\n')
    elif(regra == 12):
        #A forma de escreve do literal e num é a mesma. Muda apenas o id
        semantico.pop()#escreva
        aEscrever = semantico.pop()
        
        if(aEscrever[0] == 'id'):
            tipo = retornaTipo(aEscrever[3])

            if(tipo == '-'):
                print('Erro na linha {}: Variável não declarada'.format(aEscrever[1]))
            else:
                if(tipo == 'int'):
                    arquivo.append('printf("%d", ' + aEscrever[3] + ');')    
                elif(tipo == 'double'):
                    arquivo.append('printf("%lf", ' + aEscrever[3] + ');')
                else:
                    arquivo.append('printf("%s", ' + aEscrever[3] + ');')
        else:
            arquivo.append('printf("' + aEscrever[3] + '");')
    elif(regra == 11):
        semantico.pop()#leia
        var = semantico.pop()
        tipo = retornaTipo(var[len(var) - 1])
        
        if(tipo == '-'):
            print('Erro na linha {}: Variável não declarada'.format(var[1]))
        else:
            if(tipo == 'literal'):
                arquivo.append('scanf("%s", ' + var[len(var) - 1] + ');')
            elif(tipo == 'int'):
                arquivo.append('scanf("%d", &' + var[len(var) - 1] + ');')
            else:
                arquivo.append('scanf("%lf", &' + var[len(var) - 1] + ');')
    elif(regra == 25):
        #Exclusivo para o se, por isso farei esse tipo de exclusão
        semantico.pop()#se
        semantico.pop()#(
        op1 = semantico.pop() #id or num
        op2 = semantico.pop() #simbolo
        op3 = semantico.pop() #id or num
        semantico.pop()#)
        
        #Retornar se a operação pode ou não ser realizada
        flag = verificaTipo(op1, op3)
        if(flag == 'erro1'):
          print('Erro na linha {}: Variável não declarada'.format(op1[1]))
        elif(flag == 'erro2'):
            print('Erro na linha {}: Operando com tipos incompatíveis'.format(op1[1]))
        else:
            tipo = 'bool'
            criacaoTemporaria(tipo, arquivo, vartx, op1, op3, op2)
    elif(regra == 24):
        semantico.pop() #retirar o então do se anterior
        var = vartx[len(vartx) - 1] #vem sempre após o 24. Logo acabei de gerar a temporária
        se = 'if(' + var[2] + '){'
        arquivo.append(se)
    elif(regra == 23):
        semantico.pop() #retirar o fimse
        arquivo.append('}')
    elif(regra == 18):
        #Aqui vou pegar o primeiro e não o último
        op1 = semantico.pop(0)#1
        operacao = semantico.pop(0)#+
        op2 = semantico.pop(0)#B
        
        tipo = verificaTipo(op1, op2)
        if(tipo == 'erro1'):
          print('Erro na linha {}: Variável não declarada'.format(op1[1]))
        elif(tipo == 'erro2'):
            print('Erro na linha {}: Operando com tipos incompatíveis'.format(op1[1]))
        elif(tipo != 'literal'):
            criacaoTemporaria(tipo, arquivo, vartx, op2, op1, operacao)
            var = vartx[len(vartx) - 1]
            semantico.insert(0, [var[0], op2[1], op2[2], var[2]]) #Inserção será utilizado na Regra 17
    elif(regra == 17):
        #Essa regra trata-se obrigatoriamente de um id na hora de verificar tipos
        id = semantico.pop()
        semantico.pop()
        op = semantico.pop()
        
        tipo = retornaTipo(id[3])
        flag = 0
        if(tipo == '-'):
            print('Erro na linha {}: Variável não declarada'.format(id[1]))
        else:
            #Analisando os tipos
            if('T' in op[3]):
                flag = tiposEquivalentes(tipo, op[0])
            elif(op[0] == 'num'):
                flag = tiposEquivalentes(retornaTipoNum(op[3]), tipo)
            else:
                #op também é id
                flag = tiposEquivalentes(retornaTipo(op[3]), tipo)

            #Verificando compatibilidade
            if(flag):
                arquivo.append(id[3] + ' = ' + op[3] + ';')
            else:
                print('Erro na linha {}: Tipos diferentes para atribuição'.format(id[1]))

def criacaoTemporaria(tipo, arquivoC, arquivoV, op1, op2, op):
    tamanho = len(arquivoV)
    tx = 'T' + str(tamanho) #Criando Tx
    arq = tx + ' = ' + op1[3] + ' ' + op[3] + ' ' + op2[3] + ';' #Operação sendo realizada
    tx = [tipo, ' ', tx, ';'] #Declaração variável temporária
    arquivoC.append(arq)#Adicionando ao arquivo C
    arquivoV.append(tx)#Adicionando ao arquivo de declaração
#--------------------------------------Main--------------------------------------#
lexico()

stop = 1
fila_lexico.append(['$'])
t = 0
pilha = [0]
a = fila_lexico.pop(0)
tokenAnterior = a
semantico = []
arquivoC = []
arquivoTx = []

while stop:
  s = pilha[len(pilha) - 1]
  auxDic = tabela_action[s]
  
  if(a[0] in auxDic.keys()):
    lista = auxDic[a[0]]
    
    if lista[0] == 'S':
      t = lista[1]
      pilha.append(t)
      tokenAnterior = a
      a = fila_lexico.pop(0)

      if(a[0] != 'inicio' and a[0] != 'varinicio' and a[0] != 'varfim' and a[0] != ';' and a[0] != 'fim' and a[0] != '$'):
          semantico.insert(0, a)
    elif lista[0] == 'R':
      regra = lista[1]
      roule = gramatica_LLC[regra - 1]
      A = roule[0]
      beta = roule[2:]
      
      for i in range(0, len(beta)):
        pilha.pop()
      
      t = pilha[len(pilha) - 1]
      
      if t in tabela_goto.keys():
        auxDic = tabela_goto[t]
        
        if A in auxDic.keys():
          pilha.append(auxDic[A])
          
          if(len(semantico) > 0):
            regrasSemanticas(regra, semantico, arquivoC, arquivoTx)
    elif lista[0] == 'ACC':
      stop = 0
      escritaArquivoC(arquivoC, arquivoTx)
  else:
    #Rotina de tramento de erro de Inserção
    if(s == 0 and a[0] != 'inicio'):
      fila_lexico.insert(0, a)
      print('Erro na linha 1 coluna 0, NÃO foi identificado a palavra reservada inicio.\n')
      a = ['inicio', 1, 0]
    elif(s == 2 and a[0] != 'varinicio'):
      fila_lexico.insert(0, a)
      print('Erro na linha 2 coluna 0, NÃO foi identificado a palavra reservada varinicio.\n')
      a = ['varinicio', 1, 0]
    elif(s == 58 and a[0] != 'varfim'):
      fila_lexico.insert(0, a)
      print('Erro na linha {} coluna {}, NÃO foi identificado a palavra reservada varfim.\n'.format(a[1], a[2]))
      a = ['varfim', 1, 0]
    elif(a[0] == '$'):
      print('Erro na linha {} coluna {}, após o token {}. NÃO foi identificado a palavra reservada fim.\n'.format(tokenAnterior[1], tokenAnterior[2], tokenAnterior[0]))
      fila_lexico.insert(0, a)
      a = ['fim', tokenAnterior[1], 0]
    else:
      copia = fila_lexico.copy()
      quantAvancos = tratamentoErrosAvanco(auxDic, copia)
      
      if(quantAvancos < len(fila_lexico)):
        print('Erro na linha {} coluna {}! Próximo ao token {}.\n'.format(a[1], a[2], a[0]))
        fila_lexico = copia.copy()
        a = fila_lexico.pop(0)
      else:
        #Rotina de tramento retorna
        print('Erro na linha {} coluna {}, após o token {}.\n'.format(tokenAnterior[1], tokenAnterior[2], tokenAnterior[0]))
        stop = tratamentoErrosRetorna(a, pilha)