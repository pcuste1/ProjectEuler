def main():
    totalSum = 0
    for num in range(2,1000000):
        sumof = 0
        for digit in str(num):
            sumof += int(digit) ** 5
        if(num == sumof):
            totalSum += sumof
            print(num, " == ", sumof)
    print(totalSum)
            
main()
