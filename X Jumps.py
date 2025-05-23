for _ in range(int(input())):
    x,y=map(int,input().split())
    if x%y==0:
        print(int(x/y))
    elif x<y:
        print(x)
    else:
        s=int(x/y)
        print(s+(x-s*y))
