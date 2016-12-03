import math

def inList(strnum):
    numList =  ['1','2','3','4','5','6','7','8','9']
    for c in strnum:
         if c in numList:
             numList.remove(c)
         else:
             return False
    return True

def pan(num):
    for x in range(2,int(math.sqrt(num))):
        if num % x == 0:
            strnum = str(num)
            strnum += str(x)
            strnum += str(int(num/x))
            #print(x , "*", num/x, "=", strnum)
            if(len(strnum) == 9 and inList(strnum)):
                return num 
                print(x , "*", int(num/x), "=", num)
    return 0

def main():
    total = 0
    for num in range(10,20000):
        if pan(num):
            total += num
    print(total)
main()
