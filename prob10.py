import math

def prime(num):
    for i in range(2,max(3,int(math.sqrt(num))+1)):
        if num % i == 0 and num != 2:
            return False
    return True

def main():
    roof = int(input("Please enter the roof: "))
    total = 2
    for i in range(3,roof,2):
        if prime(i):
            total += i
    print(total)

main()

