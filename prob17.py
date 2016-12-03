'''
one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4
ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8
twenty = 6
thirty = 6
fourty = 6
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
_ hundred and _ = 10
_ thousand = 8 
'''
def countOnes(num):
    ones = {0:0,1:3,2:6,3:11,4:15,5:19,6:22,7:27,8:32,9:36,10:39,11:45,12:51,13:59,14:67,15:74,16:81,17:90,18:98,19:106}
    return ones[num]

def countTens(num):
    tens = {2:6,3:6,4:6,5:5,6:5,7:7,8:6,9:6}
    if num % 10 != 0 and num > 19:
        return countTens(num-10-(num%10))+(tens[num//10]*(num%10+1))+countOnes(num%10)
    elif num > 19:
        return countTens(num-10)+tens[num//10]*10
    else:
        return countOnes(19)

def countHundreds(num):
    return

def countThousands(num):
    return

def main():
    roof = int(input("Please enter the roof: "))
    print(roof, " :----: ", countTens(roof))
        
main()
