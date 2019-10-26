# jogo-da-velha-no-terminal
Fiz um jogo da velha em Python, que pode mudar de tamanho.

## Tela inicial
[<img src="https://raw.githubusercontent.com/gabriel-gregorio-da-silva/jogo-da-velha-no-terminal/master/imagens/print%202.png">]

- - -

## Podemos alterar o valor da variável global "tamanho" para aumentarmos o tamanho da tela atual
[<img src="https://raw.githubusercontent.com/gabriel-gregorio-da-silva/jogo-da-velha-no-terminal/master/imagens/print%201.png">](#)

- - -

A variável tamanho só pode assumir valores ímpares, e está acontecendo alguns problemas quando a escala passa de 11 em relação a formação da "o" no terminal.

Acredito que o problema está na linha 142 da versão 1.2 > __"x = x + 2.5"__.
