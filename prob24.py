def main():
    numList = [0,1,2,3,4,5,6,7,8,9]
    sortedPermutations(numList)
    print(numList)
    
def swap(a, b, numList):
    hold = numList[a]
    numList[a] = numList[b]
    numList[b] = hold

def getFirst(numList):
    length = len(numList)
    for i in range(length-2,-1,-1):
        if(numList[i] < numList[i+1]):
            return i
    return -1
        
def getCeil(first, numList):
    length = len(numList)
    ceil = first+1
    for i in range(first,length):
        if(numList[first] < numList[i] and numList[i] < numList[ceil]):
                ceil = i
    return ceil
  
def sortedPermutations(numList):

    first = 0
    ceil = 0
    count = -1
    length = len(numList)

    #print(numList)
    while(first != -1):
        count += 1

        ## Find first: rightmost number smaller than the number right of it
        first = getFirst(numList)

        ## If first == -1 then we have reached the end.
        if (count == 999999 or first == -1):
            return
        
        ## Find ceil: smallest number right of first and larger than first
        ceil = getCeil(first, numList)
        
        ## Swap first and ceil
        swap(first, ceil, numList)

        ## sort all characters right of first's original position.
        for i in range(first+1,length):
            x = i
            for j in range(i, length):
                if (numList[j] < numList[x]):
                    x = j
            swap(i, x, numList)

        #print(numList)

main()
