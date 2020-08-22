board = [['1','2','3'],['4','5','6'],['7','8','9']]
def displayed_board(board):
    print("+-----"*3, end="+\n")
    for row in range(3):
        print("|     "*3, end="|\n")
        

displayed_board(board) 

