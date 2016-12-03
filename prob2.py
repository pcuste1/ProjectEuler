def fib(a,b):
    tot = 0
    if(b < 4000000):
        tot = fib(b,a+b)
    if(b % 2 == 0):
        return tot + b
    return tot + 0

def main():
    print(fib(1,2))

main()
