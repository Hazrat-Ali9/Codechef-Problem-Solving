m=int(input())
for i in range(m):
    x,y=map(int,input().split())
    count=0
    n=list(map(int,input().split()))
    for j in n:
        if j>=y:
            count+=1
    print(count)
