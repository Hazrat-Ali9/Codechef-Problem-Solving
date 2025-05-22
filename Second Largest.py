M = int(input())

for i in range(M):
    (A, B, C) = map(int,input().split(' '))
    arr=[A,B,C]
    arr.sort()
    print(arr[-2])
    
