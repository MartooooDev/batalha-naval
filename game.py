#Projeto batalha naval - Raciocínio Algorítmico

import time, random

COORDS_V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


def gerar_tabuleiro(altura, largura):
    matriz = ['🟦'] * altura
    for linha in range(altura):
        matriz[linha] = ['🟦'] * largura
    return matriz


def printar_tabuleiro(matriz_tabuleiro, largura, altura, coords_h, COORDS_V):
    for linha in range(altura):
        linha_matriz += COORDS_V[linha] + '  '
        for coluna in range(largura):
            linha_matriz += matriz_tabuleiro[linha][coluna] + '  '
        linha_matriz += '  '
        print(linha_matriz)
    print(coords_h)


#Converte posição de letra para numero
def converter_posicao(pos_v, largura, coords_v):
    for i in range(largura):
        if(coords_v[i] == pos_v):
            #posição convertida
            pos_v = i + 1
    return pos_v


def posicionar_unidades_tabuleiro(jogador, tabuleiro, largura, altura, coords_h, coords_v):
    
    if (jogador == 'jogador'):
        for i in range(5) : 
            print('Escolha a posição da unidade: ')
            pos_h = input('Digite uma letra entre A - J: ').upper()
            pos_h_convertido = converter_posicao(pos_h, largura, coords_v)
            pos_v = input(f'Digite um número entre 1 - {largura}: ')
            
            print(pos_v, pos_h_convertido)
            
            tabuleiro[int(pos_v)-1][int(pos_h_convertido)-1] = '🛶'
            
        printar_tabuleiro(tabuleiro, largura, altura, coords_h, coords_v)
    elif (jogador == 'computador') :
        for i in range(5):
            pos_h = random.randint(1, largura)
            pos_v = random.randint(1, altura)
            tabuleiro[int(pos_v)-1][int(pos_h)-1] = '🛶'
        printar_tabuleiro(tabuleiro, largura, altura, coords_h, coords_v)

#START
coords_h = ''
# COORDS_V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print("Bem-vindo ao jogo batalha naval")
time.sleep(0.8)

tabuleiro = int(input("Qual tamanho de tabuleiro deseja utilizar para essa partida?\n 1- 5x10\n 2- 10x10\n"))
if tabuleiro == 1:
    largura = 5
    coords_h = '    1   2   3   4   5'
elif tabuleiro == 2:
    largura = 10
    coords_h = '    1   2   3   4   5   6   7   8   9   10'
else :
    print("Valor inválido")
    
altura = 10

time.sleep(0.8)
print("Tabuleiro escolhido: \n")
tabuleiro_jogador = gerar_tabuleiro(altura, largura)
printar_tabuleiro(tabuleiro_jogador, largura, altura, coords_h, COORDS_V)
tabuleiro_computador = gerar_tabuleiro(altura, largura)
posicionar_unidades_tabuleiro('jogador', tabuleiro_jogador, largura, altura, coords_h, COORDS_V)
posicionar_unidades_tabuleiro('computador', tabuleiro_computador, largura, altura, coords_h, COORDS_V)

#END
print("Jogo desenvolvido por: Elgson Nascimento, Maria Pietra, Martin Romão, Hikari Hayashida")
print("Obrigado por jogar!!")