def cheffina(n):
    free_gifts = n // 5
    return n - free_gifts

T = int(input())
for _ in range(T):
    N = int(input())
    print(cheffina(N))

