def main():
    myfile = open("primes.dat","r")
    primes = []
    for line in myfile:
        for prime in line.strip().split():
            primes.append(prime)

    #for x in range(2,100):


def f(num):
    x = len(num) - 2
    first, ceil = num[x], num[x+1]
    while num[x] > num[x+1]:
        if num[x] < ceil:
            ceil = num[x]
        x -= 1
    hold = num[0]
    num[0] = num[x]
    num[x] = hold
    print(num)
    return num

print(f(f([7,1,9])))
    
main()
