def collatz(n):
    #print(n)
    if n == 1 or n == 0:
        return 1
    if(n % 2 == 0):
        return collatz(n // 2) + 1
    return collatz(3 * n + 1) + 1

def main():
    roof = int(input("Please enter the roof: "))
    largest = [0,0]
    for i in range(1,roof+1):
        terms = collatz(i)
        #print(i, " : ", terms)
        if(terms > largest[0]):
            largest[0] = terms
            largest[1] = i
    print("The largest chain of Collatz numbers is: ", largest[1])
            
#print(collatz(13))
main()
