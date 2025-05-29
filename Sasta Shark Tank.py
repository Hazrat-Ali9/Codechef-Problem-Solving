t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a * 0.2 > b * 0.1:
        print("FIRST")
    elif a * 0.2 < b * 0.1:
        print("SECOND")
    else:
        print("ANY")

