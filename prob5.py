import math

def smallest(number):
    for i in range(2, number):
        if number % i == 0:
            return smallest(number // i)
    return number
        
def patvisor(list, total):
    for i in list:
        if(total % i != 0):
            return patvisor(list, total * smallest(i))
    return total
        
def main():
    list = [] 
    list.extend(range(1,int(input("Please enter the roof: "))))
    total = patvisor(list,2)
    print(total)
    
main()
