tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def desenhar_tabuleiro(tab):
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("---|---|---")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("---|---|---")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")

def checar_vitoria(tab):
    # 8 combinações possíveis de vitória
    combinaçoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontais
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Verticais
        [0, 4, 8], [2, 4, 6]             # Diagonais
    ]
    # Se alguma combinação tiver os mesmos 3 símbolos iguais tem um vencedor
    for a, b, c in combinaçoes:
        if tab[a] == tab[b] == tab[c]:
            return True
            
    return False

jogador_atual = 'X'
jogadas = 0
jogo_ativo = True

print("------ JOGO DA VELHA ------")

# Loop principal do jogo
while jogo_ativo:
    desenhar_tabuleiro(tabuleiro)

    # Pede a posição ao jogador atual
    escolha = int(input(f"\nJogador '{jogador_atual}', escolha uma posição livre (1-9): "))
    indice = escolha - 1  

    # verifica se o número está no intervalo correto e se a casa não foi ocupada
    if escolha >= 1 and escolha <= 9 and tabuleiro[indice] not in ['X', 'O']:
        # Marca a jogada no tabuleiro
        tabuleiro[indice] = jogador_atual
        jogadas += 1
        
        # Checa se o jogador atual venceu
        if checar_vitoria(tabuleiro):
            desenhar_tabuleiro(tabuleiro)
            print(f"\nParabéns! O jogador '{jogador_atual}' venceu!")
            jogo_ativo = False
            
        # Se deu 9 jogadas e ninguém venceu, deu Velha
        elif jogadas == 9:
            desenhar_tabuleiro(tabuleiro)
            print("\nDeu Velha! O jogo empatou.")
            jogo_ativo = False
            
        # Se não venceu e não empatou, troca a vez do jogador
        else:
            if jogador_atual == 'X':
                jogador_atual = 'O'
            else:
                jogador_atual = 'X'
                
    else:
        print("\nJogada inválida! Escolha um número de 1 a 9 que esteja livre.\n")