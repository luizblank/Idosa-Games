# Python game?

# Jogo da Velha

game = [[" "," "," "],
        [" "," "," "],
        [" "," "," "]]

moves = [11, 12, 13, 21, 22, 23, 31, 32, 33]
neg = ["n", "N", "não", "Não", "nao", "Nao", 0]

gamecontinue = True
gameround = 0
player = 1

def printgame():
    print("\n\n\n\n\n\n\n\n\n--> IDOSA GAMES <--\n")
    print("      |     |     \n",
          f"  {game[0][0]}  |  {game[0][1]}  |  {game[0][2]}  \n",
           "_____|_____|_____\n",
           "     |     |     \n",
          f"  {game[1][0]}  |  {game[1][1]}  |  {game[1][2]}  \n",
           "_____|_____|_____\n",
           "     |     |     \n",
          f"  {game[2][0]}  |  {game[2][1]}  |  {game[2][2]}  \n",
           "     |     |     \n",)
    
def verify():
    player = "O"
    
    for i in range(2):
        # Diagonais
        if(game[0][0] == player and game[1][1] == player and game[2][2] == player):
            return player
        if(game[0][2] == player and game[1][1] == player and game[2][0] == player):
            return player
        
        # Linhas
        for linha in game:
            if(linha[0] == player and linha[1] == player and linha[2] == player):
                return player
            
        # Colunas
        for j in range(3):
            if(game[0][j] == player and game[1][j] == player and game[1][j]):
                return player

        player = "X"

    return 0

def gamedecision():
    global game ,moves, gameround, player

    print("Deseja continuar jogando? (s/n)")
    decision = input("> ")
    
    if(decision in neg):
        return False
    else:
        game = [[" "," "," "],
                [" "," "," "],
                [" "," "," "]]
        moves = [11, 12, 13, 21, 22, 23, 31, 32, 33]
        gameround = 0
        player = 1
        return True
    
while(gamecontinue == True):
    printgame()

    if(player == 1):
        gameround += 1

    print(f"RODADA {gameround}")
    print(f"Jogador {player}\n")

    while True:
        print("Faça sua jogada! Ex: 12 (linha 1, coluna 2)")
        play = input("> ")
        
        if(play.isdigit()):
            if(int(play) in moves):
                break
            else:
                print("Jogada inválida, tente novamente!\n")
    
    line = int(play[0]) - 1
    col = int(play[1]) - 1

    # Fazendo a jogada e trocando o jogador
    if(player == 1):
        game[line][col] = "X"
        moves.remove(int(play))
        player = 2
    elif(player == 2):
        game[line][col] = "O"
        moves.remove(int(play))
        player = 1

    # Verificando se algum time venceu
    if(gameround >= 3):
        if(verify() == "X"):
            print("\nX venceu!\n")
            gamecontinue = gamedecision()
        elif(verify() == "O"):
            print("\nO venceu!\n")
            gamecontinue = gamedecision()