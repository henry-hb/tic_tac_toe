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
    user_spot = 0
    user_mark = "EMPTY"
    #makes sure input matches intended inputs
    while(user_spot<1 or user_spot>9):
        user_spot = int(input("Pick a spot to place your mark (1-9): "))
        if user_spot<1 or user_spot>9:
            print("Please input a number between 1 and 9")
    user_spot_str = str(user_spot)
    while(user_mark != "X" and user_mark != "O"):
        user_mark = str.upper(input("What mark are you (X or O): "))
        if user_mark != "X" and user_mark != "O":
            print("Please input either X or O")
    return (user_spot_str, user_mark)

def winner_check(spots,scores):
    #check rows
    for i in range(0,len(spots),3):
        if spots[i] == spots[i+1] == spots[i+2]:
            if spots[i] == "X":
                scores['Player 1'] +=1
                return (False,"X WINS")
            else:
                scores['Player 2'] +=1
                return (False,"O WINS")
    #check columns
    for i in range (3):
        if spots[i] == spots[i+3] == spots[i+6]:
            if spots[i] == "X":
                scores['Player 1'] +=1
                return (False, "X WINS")
            else:
                scores['Player 2'] +=1
                return (False,"O WINS")
    #check diagonals
    if spots[0] == spots[4] == spots[8]:
        if spots[0] == "X":
            scores['Player 1'] +=1
            return (False, "X WINS")
        else:
            scores['Player 2'] +=1
            return (False, "O WINS")
    elif spots[2] == spots[4] == spots[8]:
        if spots[2] == "X":
            scores['Player 1'] +=1
            return (False, "X WINS")
        else:
            scores['Player 2'] +=1
            return (False, "O WINS")
    #check full board (tie)
    full_board = True
    for i in spots:
        if i != "X" and i != "O":
            full_board = False
    if full_board:
        return (False, "TIE")
    #keep playing otherwise
    return (True, "KEEP PLAYING")

def main():
    board_spaces = [i for i in range(1,10)]
    play = True
    #Player 1 = X Player 2 = O
    scores = {'Player 1':0,'Player 2':0}
    while play:
        board(board_spaces)
        user_spot,user_mark = spot_input()
        #puts user input into correct spot
        #Checks user input and restarts loop if false
        for i in board_spaces:
            if str(i) == user_spot:
                board_spaces[i-1]=user_mark
        play,win_message = winner_check(board_spaces,scores)
    board(board_spaces)
    print(f"Player 1 score: {scores['Player 1']} \nPlayer 2 score: {scores['Player 2']} \n{win_message}")

if __name__ == "__main__":
    main()
