import math

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    high = math.ceil(x / 10)
    low = math.ceil(y / 10)
    floor = abs(low - high)
    print(floor)

