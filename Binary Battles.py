for _ in range(int(input())):
    x,y,s=map(int, input().split())
    i=1
    z=0
    while i<x:
        if 2**i==x:
            z=i
            break
        else:
            i+=1
    print(y*z + s*(z-1))
