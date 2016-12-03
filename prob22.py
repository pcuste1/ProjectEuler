def sort(names):
    small = 0
    for i in range(0,len(names)):
        for x in range(i,len(names)):
            if names[x] < names[small]:
                small = x
        holder = names[i]
        names[i] = names[small]
        names[small] = holder
            
def main():
    namesFile = open("names22.txt", "r")
    names = []
    
    for line in namesFile:
        for word in line.split(','):
            names.append(word[1:-1])
    
    #sort(names)
    names.sort()
    totSum = 0
    count = 1
    for word in names:
        letSum = 0
        for lett in word:
            letSum += ord(lett) - 64
        #print(word, ": ", count * letSum)
        totSum += letSum * count
        count += 1
    #print(count)
    print(totSum)        
    
main()    
