t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    if n <= x:
        print("YES")
    else:
        print("NO")

