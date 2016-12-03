def f(n, d): 
    x = n * 9
    z = x
    k = 1
    while z % d and k != d:
        z = z * 10 + x
        k += 1
    return k
    #return k, z / d

def main():
    #f(1,7)
    largestK = [0,0]
    for i in range(2,1001):
        k =  f(1,i)
        if k != i and k > largestK[0]:
            largestK[0] = k
            largestK[1] = i
    print(largestK)
        
main()
