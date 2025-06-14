T = int(input())  

for _ in range(T):
    N, A, B = map(int, input().split())
    odd_count = (N + 1) // 2
    even_count = N // 2
    total_duration = odd_count * B + even_count * A
    print(total_duration)

