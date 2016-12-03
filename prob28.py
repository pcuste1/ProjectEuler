def main():
    # Create the board
    board = []
    size = 1001
    for r in range(0,size):
        row = []
        for c in range(0,size):
            row.append(0)
        board.append(row)
    #print(board)    

    # Fill the board
    row, col, cor = len(board), len(board[0]), 0
    number = row * col
    total = 1
    #print(number)
    while(number > 1):
        for i in range(col-1,cor-1,-1):
            board[cor][i] = number
            number -= 1

        for i in range(cor+1, row):
            board[i][cor] = number
            number -= 1

        for i in range(cor+1, col):
            board[row-1][i] = number
            number -= 1

        for i in range(row-2,cor,-1):
            board[i][col-1] = number
            number -= 1
        total += board[cor][cor] + board[row-1][cor] + board[cor][col-1] + board[row-1][col-1]
        cor += 1
        row -= 1    
        col -= 1

        board[row-1][col-1] = 1
    """    
    for r in range(0,size):
        for c in range(0, size):
            if board[r][c] < 10:
                print("", board[r][c], end=" ")
            else:
                print(board[r][c], end=" ")
        print()
    """
    print(total)
main()
