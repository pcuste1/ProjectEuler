def f(tot,coins,count,level):
    for x in range(level,len(coins)):
        if coins[x] <= tot:
            if tot - coins[x] > 0:
                f(tot - coins[x], coins,count,coins.index(coins[x]))

            elif tot - coins[x] == 0:
                count[0] += 1
                
def main():
    count = [0]
    coins = [1,2,5,10,20,50,100,200]
    f(200,coins,count,0)
    
    print(count[0])

main()
