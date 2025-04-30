for _ in range(int(input())):
    m,x,y=map(int, input().split())
    
    a=0
    for i in range(1,m+1):
        if x*i==y:
            a+=1
    if a==1 or y==0:
        print("YES")
    else:
        print("NO")
            
