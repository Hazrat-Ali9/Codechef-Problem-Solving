for _ in range(int(input())):
    m,n,k=map(int,input().split(' '))
    
    total_candies = k*n
    
    if m%total_candies==0:
        print(m//total_candies)
    else:
    
        print((m//total_candies)+1)


