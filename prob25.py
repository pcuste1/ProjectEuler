def main():
    a,b = 1,1
    count = 2
    while(b < 10**999):
        c = b
        b = a+b
        a = c
        count += 1
    print(count)

        
main()
