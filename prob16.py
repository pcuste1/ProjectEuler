def main():
    roof = int(input("Please enter the roof: "))
    num = str(2 ** roof)
    tot = 0 
    for i in num:
        tot += int(i)

    print(tot)

main()
