# Also my solution to problem #67

def main():
    file = open("text18.txt","r")
    list = []
    for line in file:
        line = line.strip().split()
        for i in range(len(line)):
            line[i] = int(line[i])
        list.append(line)

    for i in range(len(list)-1,0,-1):
        for j in range(len(list[i])-1):
            if(list[i][j] > list[i][j+1]):
                list[i-1][j] += list[i][j]
                #print(list[i][j],end=" ")
            else:
                list[i-1][j] += list[i][j+1]
                #print(list[i][j+1],end=" ")
        #print()
    print(list[0])
main()
