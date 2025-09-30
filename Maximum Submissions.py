t = int(input())
for _ in range(t):
    x = int(input())
    available_time = x * 60 - 5
    print(available_time // 30)

