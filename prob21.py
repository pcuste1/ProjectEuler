import math

def d(num):
    dnum = 0
    dnum2 = 0
    for i in range(1,num):
        if num % i == 0:
            dnum += i
            
    for i in range(1,dnum):
        if dnum % i == 0:
            dnum2 += i

    if (dnum2 == num and dnum2 != dnum):
        print(dnum)
        return dnum
    return 0
            
def main():
    sum = 0
    for i in range(1,10000):
        if d(i):
            print(i)
            sum += i
    print(sum)
            
main()
