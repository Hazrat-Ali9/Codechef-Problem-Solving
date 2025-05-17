F = int(input())
for i in range(F):
    (a, b, p) = map(int,input().split(' '))
    
    sum = (a-b)*1 
    if (b*3)-sum >= p:
        print("Pass")
    else:
        print("Fail")
