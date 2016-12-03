import math

def getNumFactors(num):
    factors = 0
    for i in range(1,max(2,int(math.sqrt(num+1)))):
        if num % i == 0:
            factors += 2
    return factors
            
def main():
    roof = int(input("Please enter the roof: "))
    factors,value,count,test = 0,1,1,10
    while(factors <= roof):
        factors = 0
        factors = getNumFactors(value)
        count += 1
        value += count
        if(factors == test):
            print(factors, ": ", value)
            test += 10
    print(value - count)
        
    
main()
