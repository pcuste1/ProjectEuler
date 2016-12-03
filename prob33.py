def main():
    total = 1
    for n in range(10,100):
        for d in range(n+1,100):
            n_x = int(str(n)[0])
            n_y = int(str(n)[1])
            d_x = int(str(d)[1])
            d_y = int(str(d)[0])
            if(d_x != 0 and n_y == d_y and n/d == n_x/d_x):
                total *= n_x / d_x
                print(n_x, "/", d_x)
    print(total)
                
main()
