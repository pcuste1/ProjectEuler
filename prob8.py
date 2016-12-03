def main():
    roof = int(input("Please enter the roof: "))
    greatestTotal = 0
    file = open("text.txt", "r")
    numList = []
    for line in file:
        for num in line.strip():
            numList.append(int(num))

    for i in range(len(numList)):
        total = 1
        for j in range(i,min(i+roof,len(numList))):
            total *= numList[j]
        if(total > greatestTotal):
            greatestTotal = total
            
    print(greatestTotal)
    
main()
