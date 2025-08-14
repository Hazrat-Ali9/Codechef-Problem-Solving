T = int(input())

for _ in range(T):
    
    K, X = map(int, input().split())
    
    total_days = K * 7
    
    remaining_days = total_days - X
    
    print(remaining_days)

