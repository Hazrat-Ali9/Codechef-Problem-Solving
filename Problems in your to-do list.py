m = int(input())

for i in range(m):
    n = int(input())
    
    temp = 0
    p = input()
    
    q = p.split()    
    for a in range(n):
        if int(q[a]) >= 1000:
            temp += 1
    
    print(temp)

