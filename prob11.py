# The grid is 20 x 20
def adjacent(grid, row, col):
    greatestTotal, total = 0,1
    for r in range(-1,2):
        for c in range(-1,2):
            total = grid[row][col] * extention(grid,row,col,r,c,3)
            if total > greatestTotal:
                greatestTotal = total
    return greatestTotal
            
def extention(grid, row, col, rowMod, colMod, distance):
    row = row+rowMod
    col = col+colMod
    if(row >= 20 or row < 0 or col >= 20 or col < 0 or distance == 0
       or (rowMod == 0 and colMod == 0) ):
        return 1
    return grid[row][col] * extention(grid, row, col, rowMod, colMod, distance-1)

    
def main():
    file = open("text11.txt", "r")
    grid = []
    for line in file:
        numList = []
        for num in line.strip().split():
            numList.append(int(num))
        grid.append(numList)

    greatestTotal, total = 0, 0    
    for row in range(20):
        for col in range(20):
            total = adjacent(grid,row,col)
            if total > greatestTotal:
                greatestTotal = total
    print(greatestTotal)

main()
