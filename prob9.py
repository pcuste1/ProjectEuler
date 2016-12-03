def main():
    roof = int(input("Please enter the roof: "))
    for a in range(1,roof):
        for b in range(1,roof - a):
            c = roof - a - b
            if(a ** 2 + b ** 2 == c ** 2):
                print(a, ", ", b, ", ", c, " : Product abc : ", a * b * c)

main()

