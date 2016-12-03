def main():
    file = open("text.txt", "r")
    numList = []
    sum = 0
    for line in file:
        numList.append(int(line))
        #sum += int(line[-10:0])
        sum += int(line)
        
    print(str(sum)[0:10])
main()
