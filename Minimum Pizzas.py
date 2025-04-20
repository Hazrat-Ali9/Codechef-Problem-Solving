for _ in range(int(input())):
    m,n=map(int, input().split())
    p=(m*n)
    if p%4==0:
        print(int(p/4))
    else:
        print(int(p/4)+1)
# Minimum Pizzas 