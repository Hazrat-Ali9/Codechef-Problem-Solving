T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    total = A + B + C
    lowest = min(A, B, C)
    print(total - lowest)

