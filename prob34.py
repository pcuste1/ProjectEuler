def fac(n):
    if n <= 1:
        return 1
    else:
        return fac(n-1) * n

def main():
    total = 0
    for i in range(3,1000000):
        c = 0
        for digit in str(i):
            c += fac(int(digit))
        if c == i:
            total += i
            print(i)
    print(total)
    
main()
