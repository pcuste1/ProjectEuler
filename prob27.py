import math

# create a list of primes
def prime():
    primeList = []
    myFile = open("primes.dat", "r")
    for line in myFile:
        for num in line.strip().split():
            if(int(num) < 1000):
                primeList.append(int(num))
    return primeList

#print(prime())

def main():
    primes = prime()
    product = 0
    aMax, bMax, nMax = 0, 0, 0

    #loop all |a| < 1000 and all |b| < 1000
    for a in range(-1000,1000):
        for b in primes:

            # n**2 + a*n + b = x
            n,x = 0,2
            
            # keep looping n until x isn't in list of primes
            while x in primes: 
                
                #print(x)
                x = n ** 2 + a * n + b
                n += 1

                # keep track of largest n value achieved.
            if(n > nMax):
                
                # store the product of the largest a and b.
                product = a * b
                aMax, bMax, nMax = a, b, n
                
    # that is the answer
    print(product, " ", aMax," ", bMax," ", nMax)

main()
