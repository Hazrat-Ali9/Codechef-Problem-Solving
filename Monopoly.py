m=int(input())
for i in range(m):
    a,b,c,d=map(int,input().split())
    if a+b+c<d:
        print("yes")
    elif b+c+d<a:
        print("yes")
    elif a+b+d<c:
        print("yes")
    elif a+c+d<b:
        print("yes")
    else:
        print("no")
