for _ in range(int(input())):
    a,b=map(int, input().split())
    c=0
    if a>=b:
        i=True
        ans=0
        while i==True:
            if ans<=a:
                ans=c*b
                c+=1
            else:
                i=False
    if not c:
        print(c)
    else:print(c-2)
        
