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
    user_input = str(input("Pick a spot to place your mark: "))
    return user_input
def winner_check():
    pass
def main():
    board_spaces = [i for i in range(1,10)]
    board(board_spaces)
    

if __name__ == "__main__":
    main()