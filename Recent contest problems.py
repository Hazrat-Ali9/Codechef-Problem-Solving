m = int(input())

for i in range(m):
    n = int(input())
    
    s = input()
    b = s.split()
    
    temp = 0
    contest = 0
    for j in range(n):
        if b[j] == "START38":
            temp += 1
        else:
            contest += 1
    print(temp, contest)    
