import math

def abundant(num):
    sum = 0
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            sum += i
            if (num // i != num and num // i != i):
                sum += num // i
    if sum > num:
        return True
    return False

def abundantSum(num, abundants, abundants_set):
    for i in abundants:
        if (num-i in abundants_set):
            return True
        if (i > num):
            return False
    return False
        
def main():
    total = 0
    abundants = []
    for i in range(0,28123):
        if abundant(i):
            abundants.append(i)
    print("-------------------------------------------------------------------------------")
    abundants_set = set(abundants)
    for i in range(0,28123):
        if not abundantSum(i, abundants, abundants_set):
                total += i
    print("-------------------------------------------------------------------------------")
    print(total)
    
main()
