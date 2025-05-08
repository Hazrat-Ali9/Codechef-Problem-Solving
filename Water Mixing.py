for _ in range(int(input())):
    x,y,z,m=map(int,input().split())
    if(x<=y):
        if(y-x<=z):
            print("yes")
        else:
            print("no")
    else:
        if(x-y<=m):
            print("yes")
        else:
            print("no")
