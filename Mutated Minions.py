t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a = [x + k for x in a]

    count = sum(1 for x in a if x % 7 == 0)

    print(count)

