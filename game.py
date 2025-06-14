#Projeto batalha naval - Raciocínio Algorítmico
#Códigos feitos majoritariamente por meio da extensão Live Share

import time, random, os, platform

#Coordenadas verticais (qtde sempre é 10, então definido como variável constante no código)
COORDS_V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

#Limpeza de terminal p/ windows e linux
def limpar_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

#Função de gerar tabuleiro vazio
def gerar_tabuleiro(altura, largura):
    matriz = ['🟦'] * altura
    for linha in range(altura):
        matriz[linha] = ['🟦'] * largura
    return matriz

#Função para printar tabuleiro sem mostrar as coordenadas com unidades (usado para printar o campo do computador durante o ataque do jogador)
def printar_tabuleiro_oculto(matriz_tabuleiro, largura, altura, coords_h, coords_v):
    for linha in range(altura):
        linha_matriz = coords_v[linha] + '  '
        for coluna in range(largura):
            celula = matriz_tabuleiro[linha][coluna]
            if celula == '🛶':
                celula = '🟦'
            linha_matriz += celula + '  '
        print(linha_matriz)
    print(coords_h)

#Função para printar tabuleiro completo com unidades posicionadas (Para debug ou para o jogador ver seu próprio campo)
def printar_tabuleiro(matriz_tabuleiro, largura, altura, coords_h, coords_v):
    linha_matriz = ''

    for linha in range(altura):
        linha_matriz += coords_v[linha] + '  '
        for coluna in range(largura):
            linha_matriz += matriz_tabuleiro[linha][coluna] + '  '
        linha_matriz += '  '
        print(linha_matriz)
        linha_matriz = ''
    print(coords_h)


#Função que converte posição de letra para numero
def converter_posicao(pos_v, largura, coords_v):
    for i in range(altura):
        if(coords_v[i] == pos_v):
            #posição convertida
            pos_v = i + 1
    return pos_v

#Função para posicionamento de unidades
def posicionar_unidades_tabuleiro(jogador, tabuleiro, largura, altura, coords_v): #,coords_h se precisar printar tabuleiro completo
    
    if (jogador == 'jogador'):
        for i in range(5) : 
            print('Escolha a posição da unidade: ')
            pos_v = input('Digite uma letra entre A - J: ').upper().strip()
            pos_v_convertido = converter_posicao(pos_v, largura, coords_v)
            pos_h = input(f'Digite um número entre 1 - {largura}: ').upper().strip()
            time.sleep(0.5)

            # print(pos_h, pos_v_convertido)
            
            tabuleiro[int(pos_v_convertido)-1][int(pos_h)-1] = '🛶'
            
        # printar_tabuleiro(tabuleiro, largura, altura, coords_h, coords_v)
    elif (jogador == 'computador') :
        for i in range(5):
            pos_v = random.randint(1, largura)
            pos_h = random.randint(1, altura)
            tabuleiro[int(pos_h)-1][int(pos_v)-1] = '🛶'
        # printar_tabuleiro(tabuleiro, largura, altura, coords_h, coords_v)


#Função para contar unidades restantes no tabuleiro
def contar_barcos(tabuleiro):
    """Conta quantos barcos restam no tabuleiro."""
    return sum(linha.count('🛶') for linha in tabuleiro)

#Função para ataque do jogador e computador
def atacar(tabuleiro_alvo, largura, altura, coords_v, jogador):
    while True:
        if jogador == "Jogador":
            pos_v = input('Escolha a linha (letra A-J): ').upper()
            pos_v_convertido = converter_posicao(pos_v, altura, coords_v)
            pos_h = input(f'Escolha a coluna (1-{largura}): ')
            try:
                linha = int(pos_v_convertido) - 1
                coluna = int(pos_h) - 1
                if tabuleiro_alvo[linha][coluna] in ['💥', '❌']:
                    print("Você já atacou essa posição. Escolha outra.")
                    continue
                break
            except (ValueError, IndexError):
                print("Coordenada inválida. Tente novamente.")
        else:
            linha = random.randint(0, altura - 1)
            coluna = random.randint(0, largura - 1)
            if tabuleiro_alvo[linha][coluna] in ['💥', '❌']:
                continue
            break

    if tabuleiro_alvo[linha][coluna] == '🛶':
        for icone in ["💣", "💥", "🔥"]:
            tabuleiro_alvo[linha][coluna] = icone
            limpar_terminal()
            print(f"Ataque do {jogador}.")
            if (jogador == 'Jogador') :
                printar_tabuleiro_oculto(tabuleiro_alvo, largura, altura, '', coords_v)
            else:
                printar_tabuleiro(tabuleiro_alvo, largura, altura, coords_h, COORDS_V)
            time.sleep(0.7)
        tabuleiro_alvo[linha][coluna] = '💥'
        limpar_terminal()
        if (jogador == 'Jogador') :
            printar_tabuleiro_oculto(tabuleiro_alvo, largura, altura, '', coords_v)
        else:
            printar_tabuleiro(tabuleiro_alvo, largura, altura, coords_h, COORDS_V)
        limpar_terminal()
        print(f"{jogador} acertou um barco!")
        return True
    else:
        for icone in ["💣", "🌊", "❌"]:
            tabuleiro_alvo[linha][coluna] = icone
            limpar_terminal()
            print(f"Ataque do {jogador}.")
            if (jogador == 'Jogador') :
                printar_tabuleiro_oculto(tabuleiro_alvo, largura, altura, '', coords_v)
            else:
                printar_tabuleiro(tabuleiro_alvo, largura, altura, coords_h, COORDS_V)
            time.sleep(0.7)
        tabuleiro_alvo[linha][coluna] = '❌'
        limpar_terminal()
        if (jogador == 'Jogador') :
                printar_tabuleiro_oculto(tabuleiro_alvo, largura, altura, '', coords_v)
        else:
            printar_tabuleiro(tabuleiro_alvo, largura, altura, coords_h, COORDS_V)
        limpar_terminal()
        print(f"{jogador} errou o ataque.")
        return False
    
    
#START
coords_h = ''
COORDS_V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print("🚩Bem-vindo ao jogo batalha naval")
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
posicionar_unidades_tabuleiro('jogador', tabuleiro_jogador, largura, altura, COORDS_V) #, coords_h antes de COORDS_V para ver unidades
print('')
posicionar_unidades_tabuleiro('computador', tabuleiro_computador, largura, altura, COORDS_V) #, coords_h antes de COORDS_V para ver unidades


#Jogo em loop até um dos jogadores vencer
while True:
    
    print("\nSeu tabuleiro:")
    printar_tabuleiro(tabuleiro_jogador, largura, altura, coords_h, COORDS_V)
    print("\nTabuleiro do computador:")
    printar_tabuleiro_oculto(tabuleiro_computador, largura, altura, coords_h, COORDS_V)

    print("\nSua vez de atacar!")
    atacar(tabuleiro_computador, largura, altura, COORDS_V, "Jogador")
    if contar_barcos(tabuleiro_computador) == 0:
        print("Parabéns! Você venceu!")
        break

    print("\nVez do computador atacar!")
    atacar(tabuleiro_jogador, largura, altura, COORDS_V, "Computador")
    if contar_barcos(tabuleiro_jogador) == 0:
        print("O computador venceu!")
        break
        
#END
print("Jogo desenvolvido por: Elgson Nascimento, Maria Pietra, Martin Romão, Hikari Hayashida")
print("Obrigado por jogar!!")