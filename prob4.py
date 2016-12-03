def palindrome(string):
    for i in range(len(string) // 2):
        #print(string[i], " == ", string[-1-i])
        if(string[i] != string[-1-i]):
            return False
    return True

def main():
    largest = 0
    for i in range(100,1000):
        for j in range(100, 1000):
            if(palindrome(str(i*j))):
                largest = largest if (largest > i*j) else i*j
                # print(i*j ," = ", i, " X ", j)
    print(largest)
#palindrome("9009")                
main()
