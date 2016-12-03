def main():
    roof = int(input("Please enter the roof: "))
    SumOfSquares = 0
    SquareOfSums = 0
    for i in range(roof + 1):
        SumOfSquares += i ** 2
        SquareOfSums += i
    print(SquareOfSums ** 2 - SumOfSquares) 
    
main()
