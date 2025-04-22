for _ in range(int(input())):
    m=list(map(int, input().split()))
    if m[0]*m[1]>m[2]*m[3]:
        print("No")
    else:
        print("Yes")
