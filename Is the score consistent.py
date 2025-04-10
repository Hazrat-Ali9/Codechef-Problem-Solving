for i in range(int(input())):
    m,n = map(int, input().split())
    o,p = map(int, input().split())
    if(o>=m and p>=n):
        print("Possible")
    else:
        print("Impossible")

