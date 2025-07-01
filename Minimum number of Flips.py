def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n % 2 == 1:
        print(-1)
        return

    positive = sum(1 for x in a if x == 1)
    negative = n - positive
    half = n // 2

    print(min(abs(half - positive), abs(half - negative)))


T = int(input())
for _ in range(T):
    solve()

