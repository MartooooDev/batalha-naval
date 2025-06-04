#Projeto batalha naval - Raciocínio Algorítmico

import time, ast

def gera_tabuleiro(altura, largura):
    matriz = ['🟦'] * altura
    for linha in range(altura):
        matriz[linha] = ['🟦'] * largura
    return matriz


#START
print("Bem-vindo ao jogo batalha naval")
tabuleiro = int(input("Qual tabuleiro deseja utilizar para essa partida?\n 1- 5x10\n 2- 10x10\n"))
if tabuleiro == 1:
    largura = 5
elif tabuleiro == 2:
    largura = 10
else :
    print("Valor incorreto para tabuleiro")
    
altura = 10


print("Tabuleiro escolhido: ")
matriz = gera_tabuleiro(altura, largura)
for linha in matriz:
        print(linha)



#END
print("Jogo desenvolvido por: Elgson Nascimento, Maria Pietra, Martin Romão, Hikari Hayashida")
print("Obrigado por jogar!!")