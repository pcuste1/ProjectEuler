import math

def prime(num):
    for i in range(2,max(3,int(math.sqrt(num))+1)):
        if num % i == 0 and num != 2:
            return False
    return True

def main():
    roof = int(input("Please enter the roof: "))
    primeCount, totCount = 0,1
    while(primeCount < roof):
        totCount += 1
        if prime(totCount):
            primeCount += 1

    print(totCount)

main()
