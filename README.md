# Compilador
Desenvolvimento de um compilador.


## Sobre
Este é uma atividade prática da disciplina de compiladores e foi dividido em três partes.
* Análise Léxica e tabela de símbolos;
* As outras duas vou colocar aqui conforme a professora for liberando.

>> Observação: o compilador desenvolvido é para linguagem MGol.

## Funcionamento
### Parte 1: Análise Léxica
* A tabela de símbolos deve conter todas as palavras chaves da linguagem;
* Desenvolver uma função/procedimento/objeto chamado *léxico*, que ao ser invocado efetuará a leitura de um lexema e retornará uma estrutura por chamada contento três campos: lexema, token e tipo;
* Efeturá a leitura do código fonte caracter por caracter;
>> Obs.: Vou adicionar a tabela de tokens que são reconhecidos pela linguagem, a tabela de palavras chaves e o código fonte utilizado.
* Se o token reconhecido for diferente de identificador mostrar na tela os dados reconhecidos (lexema, token, tipo);
* Se o token reconhecido já estiver na tabela, retornas as informações já conhecidas. Caso não, inserir na tabela de símbolos e retornar a estrutura: token, lexema e tipo;
* O programa deve ler o código fonte e apresentar na tela o token, lexema e o tipo. Quando não for possível, deve imprimir *ERRO* seguido da linha e coluna;
* Comentários, espaço em branco, tabulação e salto de linha deverão ser reconhecidos porém ignorados.

## Como fazer
### Parte 1: Análise Léxica
1. Desenvolver o autômato (DFA), com base na gramática (que no caso seria a coluna características da tabela de tokens).
2. Criar uma tabela de transição com base nos estados do autômato. O autômato é quem vai definir o reconhecimento da linguagem, então implemente-o em uma estrutura que consiga manipular de forma fácil.
3. Implemente os tópicos descrito em *Funcionamento: Parte 1* e terá a fase de análise léxica pronta.


>>Já realizei algumas alterações localmente, porém preciso verificar umas questões antes de atualizar este repositório. Pretendo atualizá-las assim que possível, tanto as informações quanto um refatoramento do código. Pretendo também separar as funções e deixá-las mais abstratas.
