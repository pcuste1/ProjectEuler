def main():
    fac = 1
    for i in range(100,1,-1):
        fac = fac * i
    fac = str(fac)
    sumNum = 0
    for i in fac:
        sumNum += int(i)
        
    print(sumNum)
    

main()
