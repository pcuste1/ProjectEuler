import math

def LEE(Lee):
     for lee in range(2,max(3,int(math.sqrt(Lee))+1)):
          #print(Lee, " % ", lee, " = ", Lee % lee)
          if(Lee % lee == 0): 
               return 0
     return Lee

def primeFactor(roof):
     total = 1
     for i in range(2,roof):
          if LEE(i) and roof % i == 0:
               total = total * i
          if(total == roof):
               return i

def main():
    roof = int(input("Enter the roof: "))
    print(primeFactor(roof))
            
main()
