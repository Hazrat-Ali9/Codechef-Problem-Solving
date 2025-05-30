T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    total_students = X * Y
    if Z > total_students / 2:
        print("YES")
    else:
        print("NO")

