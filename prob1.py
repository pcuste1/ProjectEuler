def main():
    roof = int(input("Enter the roof: "))
    count = 0
    for i in range(roof):
        if(i % 3 == 0 or i % 5 == 0):
            count += i
    print(count)
    
main()
