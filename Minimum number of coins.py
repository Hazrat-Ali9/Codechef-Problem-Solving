for _ in range(int(input())):
    n=int(input())
    coin=int(n/10)
    coin2=n-coin*10
    coin3=int(coin2/5)
    sol=n-coin3*5-coin*10
    if sol>0:
        print(-1)
    else:
        print(coin3+coin)

