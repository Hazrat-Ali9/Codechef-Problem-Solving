t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    
    total_cost = n * x
    
    if k >= total_cost:
        print("YES")
    else:
        print("NO")

