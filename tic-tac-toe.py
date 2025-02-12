def board(spots):
    row1 = [spots[0],"|",spots[1],"|",spots[2]]
    row2 = ["-----"]
    row3 = [spots[3],"|",spots[4],"|",spots[5]]
    row4 = ["-----"]
    row5 = [spots[6],"|",spots[7],"|",spots[8]]
    game_board = [row1, row2, row3, row4, row5]
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            print(game_board[i][j],end="")
        print()

def spot_input():
    user_input = [str(input("Pick a spot to place your mark: ")),str.upper(input("What mark are you: "),)]
    return user_input
def winner_check():
    pass
def main():
    board_spaces = [i for i in range(1,10)]
    board(board_spaces)
    play = True
    scores = {'Player 1':0,'Player 2':0}
    while play:
        user_spot = spot_input()
        #puts user input into correct spot
        for i in board_spaces:
            if str(i) == user_spot[0]:
                board_spaces[i-1]=user_spot[1]
        if(winner_check):
            play = False
        print(f"Player 1 score: {scores['Player 1']} \nPlayer 2 score: {scores['Player 2']}")

if __name__ == "__main__":
    main()