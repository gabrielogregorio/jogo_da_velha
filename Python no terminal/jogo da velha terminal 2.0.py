#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__       =  ' Gabriel Gregório da Silva '
__email__        =  ' gabriel.gregorio.1@outlook.com '
__description__  =  ' Jogo da velha simples no terminal '
__status__       =  ' Desenvolvido '
__DATE__         =  ' 09/06/2019 00:36'
__version__      =  ' 1.0 '

from copy import deepcopy
import os

# EU SOU IMPORTANTE, AQUI QUE VOCÊ PODE AUMENTAR A ESCALA DO JOGO!
# tamanho do tabuleiro
global tamanho
# SÃO VALORES ÁMPARES
tamanho = 5

# IMPEDIR QUE O USUÁRIO DIGITE UM NUMERO PAR
if tamanho % 2 == 0:
  tamanho = tamanho+1

# DEU VELHA
global velha
velha = 0

# ALGUÉM GANHOU?
global ganhou
ganhou = "nao"

# EDITAR TABULEIRO REAL
global a
a = []

# POSIÇÕES VENDEDORAS NO FOR
global d

# VEZ DE QUEM?
global vez
vez = 'x'

# POSIÇÕEO PARA MARCAR *
global posicao
posicao = 0

# Tabuleiro final
global fixa
fixa = []

# LINHAS / COLUNAS DE TODAS AS POSIÇÕES
global lin_col
lin_col = [ [0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

# É USADO PARA ATUALIZAR AS POSIÇÕES DE ACORDO COM A ESCALA "tamanho"
chi = []
full = []

# TODAS AS POSIÇÕES VENCEDORAS
cond_v  = [ [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6] ]

# Cópia das condições vencedoras
cond_v_copia = deepcopy(cond_v)

# CRIANDO A PRECIOSA TELA - NUMEROS E ESPAÁ‡OS
for tam in range(tamanho**2*9):
  fixa.append(' ')

# CALCULA A POSIÇÕEO CENTRAL DO TABULEIRO DE ACORDO COM A ESCALA
def calc_centro(tamanho,linha,coluna):
  linha   = int(linha)
  coluna  = int(coluna)
  tamanho = int(tamanho)
  return int((((tamanho**2 * 3) * linha) + ((tamanho * 3) * (tamanho/2+0.5))-(tamanho/2+0.5)) - ((2-coluna)*tamanho))

# CONVERTER AS POSIÇÕES VENCEDORAS PARA A NOVA REALIDADE
for lisa in cond_v:
  for item in lisa:
    full.append( int(calc_centro(tamanho , lin_col[item][0] , lin_col[item][1] )) )
  chi.append(full)
  full = []

# MARCA A POSIÇÕEO X ou O
def marcar_pos(lin,col):
  pos = calc_centro(tamanho,lin,col)

  if vez =='x':
    # CASO O TABULEIRO SEJA NA ESCALA 1
    if tamanho == 1:
      return pos,pos

    # CASO SEJA MAIOR QUE 1
    x = 3
    y = 1
    lateral_1 = [] # LATERAIS PARA MARCAR \
    lateral_2 = [] # LATERAIS PARA MARCAR /
    while y*2+1 <= tamanho:
      p1 = tamanho*x+y
      p2 = tamanho*x-y

      # ADICIONAR OS DADOS NA LISTA PROVISÁ“RIA
      lateral_1.append(int(pos-p1))
      lateral_1.append(int(pos+p1))
      lateral_2.append(int(pos+p2))
      lateral_2.append(int(pos-p2))

      y=y+1
      x = x+3

    # CONVERTER PARA TUPLA
    lateral_1 = tuple(lateral_1)
    lateral_2 = tuple(lateral_2)
    return pos , lateral_1 , lateral_2

  else:
    # CASO O TABULEIRO SEJA NA ESCALA 1
    if tamanho == 1:
      return pos,pos

    lista_1 = []
    lista_2 = []

    ciclo = int(tamanho/2 - 0.5)
    base = tamanho * (tamanho+(ciclo-1)) - ciclo

    # Primeira lista
    for x in range(tamanho):
      lista_1.append(base+x)

    # Segunda lista
    rever = tamanho - 2
    if rever < 0:
      lista_2.append(ciclo)
    else:
      x = 1
      multiplicador = 1
      lista_2.append(ciclo)
      while x <= rever:
        loop = (tamanho*3*multiplicador)
        lista_2.append(loop-ciclo)
        lista_2.append(loop+ciclo)
        x = x + 2.5
        multiplicador = multiplicador + 1

      # inverter lista_2 > Os numeros oscilam entre positivo e negativo
      inv = []
      for u in lista_2:
        inv.append(u*-1)
      lista_2 = lista_2+inv

      sd = []
      for u in lista_2:
        sd.append(u+pos)
      lista_2 = deepcopy(sd)


      # inverter lista_1 > Os numeros oscilam entre positivo e negativo
      inv = []
      for u in lista_1:
        inv.append(u*-1)
      lista_1 = lista_1+inv

      sd = []
      for u in lista_1:
        sd.append(u+pos)
      lista_1 = deepcopy(sd)

    # Convertendo todo mundo par tupla
    lateral_1 = tuple(lista_1)
    lateral_2 = tuple(lista_2)
    return pos , lateral_1 , lateral_2


def fazer_tabuleiro():
  global fixa    # TABULEIRO
  global tamanho # ESCALA DO TABULEIRO
  global d       # POSIÇÕEO QUE GANHOU
  global ganhou  # ALGUÉM GANHOU
  global posicao # POSIÇÕEO PARA MARCAR
  global a       # EDITA A POSIÇÕES
  global vez     # VEZ DE QUEM?
  global lin_col # TODAS AS LINHAS E COLUNAS, SEGUINDO O MODELO SIMPLES DO JOGO DA VELHA

  os.system("cls")
  print("feito por Gabriel Gregório da Silva \nMovimentação [w,a,s,d] + enter | seleção f | ?")

  # Vamos copiar o tabuleiro real
  l = deepcopy(fixa)

  # NinguÁ©m ganhou ainda
  if ganhou == "nao":
    lista = marcar_pos(lin_col[posicao][0],lin_col[posicao][1])

    l[ lista[0] ] = vez
    
    if vez == 'x':
      # Se tem mais de duas posições
      if tamanho > 2:
        for lat in lista[1]:
          l[int(lat)] = "\\"

        for lat in lista[2]:
          l[int(lat)] = "/"
    if vez == "o":
      if tamanho > 2:
        for lat in lista[1]:
          l[int(lat)] = "-"

        for lat in lista[2]:
          l[int(lat)] = "|"

  # AlguÁ©m ganhou!
  elif ganhou == "sim":
    # Marcar as trás primeiras casas vencedoras
    for x in range(3):
      lista = marcar_pos(lin_col[ d[x] ][0],lin_col[ d[x]][1])
      l[int(lista[0])] = vez

      if tamanho > 2:
        for lat in lista[1]:
          l[int(lat)] = "#"
        for lat in lista[2]:
          l[int(lat)] = "#"

  # Criação visual do tabuleiro
  for w in range(3):              # LINHAS
    for z in range(tamanho):      # SUBLINHAS
      for x in range(3):          # COLUNA
        for y in range(tamanho):  # SUBCOLUNA
          if y == tamanho-1 and x != 2:
            m = "|"
          else:
            m = ""
          print(str(l[y + (tamanho * x) + (tamanho * 3 * z) + (tamanho * tamanho * 3 * w)])+m, end=" ")
      print("")
    if w != 2:
      print("-"*((tamanho*2)*3+1))

fazer_tabuleiro()

# LOOP DO PROGRAMA
while True:
  clique = input("Jogador {}: ".format(vez))
  clique = clique.lower()

  # TECLA ESCOLHIDA
  if clique == "w":
    if posicao>2:
      posicao = posicao - 3

  elif clique == "s":
    if posicao < 6:
      posicao = posicao + 3

  elif clique == "a":
    if posicao != 0  and posicao != 3 and posicao != 6:
      posicao = posicao - 1

  elif clique == "d":
    if posicao != 2 and posicao != 5 and posicao != 8:
      posicao = posicao + 1

  elif clique == "?":
    os.system("clear")
    print("""
Descrição
Jogo da velha simples para terminal

Dica
Aumentar ou diminuir o tamanho do jogo
Altere o valor da variável 'tamanho' no código fonte

Autor
Gabriel Gregório da Silva

Email
gabriel.gregorio.1@outlook.com """)
    i = input("\nContinuar...")


  # MARCAR COM A VEZ
  elif clique == "f":
    if fixa[int(calc_centro(tamanho, lin_col[posicao][0] ,lin_col[posicao][1]))] == " ":
      lista = marcar_pos(lin_col[posicao][0],lin_col[posicao][1])
      fixa[int(lista[0])] = vez
      velha = velha + 1

      if vez=="x":
        # Se tem mais de duas posições
        if tamanho > 2:
          for lat in lista[1]:
            fixa[int(lat)] = "\\"

          for lat in lista[2]:
            fixa[int(lat)] = "/"
      else:
        # Se tem mais de duas posições
        if tamanho > 2:
          for lat in lista[1]:
            fixa[int(lat)] = "-"

          for lat in lista[2]:
            fixa[int(lat)] = "|"
      manter = 0

      # VERIFICA SE O JOGADOR PODE TER GANHADO
      for y in chi:
        if fixa[y[0]] == vez and fixa[y[1]] == vez and fixa[y[2]] == vez:

          d = cond_v_copia[manter]
          ganhou = "sim"
          fazer_tabuleiro()

          print("Jogador {} vocá ganhou".format(vez.upper()))
          break # PARAR NA PRIMEIRA OCORRÊNCIA
        manter = manter+1

      # ATUALIZA A POSIÇÕEO
      if vez == "x":
        vez = "o"
      else:
        vez = "x"

  # VERIFICA SE DEU VELHA
  if ganhou == "nao" and velha == 9:
   ganhou = "velha"

  # SE NINGUÉM GANHOU AINDA
  if ganhou == "nao":
    fazer_tabuleiro()

  # SE DEU VELHA
  elif ganhou == "velha":
    print("DEU VELHA AMIGOS")
    i = input("\nContinuar...")
    break

  # ALGUÉM GANHOU
  else:
    al = input("\nObrigado por jogar! Que tal favoritar meu projeto no github? []")
    break
