T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    total = (10 * X) + (90 * Y)
    print(total)
