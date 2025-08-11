T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    if A + B == C:
        print("YES")
    else:
        print("NO")

