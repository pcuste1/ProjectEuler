import time

def main():
    start_time = time.time()
    gridSize = int(input("Please enter the grid size: "))
    #num = moverecur(0,0,0,gridSize)
    gridList = [1] * (gridSize + 1)
    custerAlgo(gridList)
    print(gridList[gridSize])
    print("--- %s seconds ---" % (time.time() - start_time))

def custerAlgo(gridList):
    for c in range(1,len(gridList)):
        for i in range(1,len(gridList)):
            gridList[i] = gridList[i] + gridList[i-1]

    
def moverecur(row,col,num,maximum):
    if(row == maximum or col == maximum):
        return num + 1
    num = moverecur(row+1, col,num,maximum)
    num = moverecur(row, col+1,num,maximum)
    return num

main()

