n = int(input())
max=0
x1=0
x2=0

for i in range(n):
    a, b = map(int, input().split())
    x1 += a
    x2 += b
    diff=x1-x2
    
    if diff>0 and diff>max:
        max=diff
        leader=1

    elif diff<0 and abs(diff)>max:
        max=abs(diff)
        leader=2
print(leader,max)
