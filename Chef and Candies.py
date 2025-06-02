import math

m = int(input())
for _ in range(m):
    n, x = map(int, input().split())
    if x >= n:
        print(0)
    else:
        candies = n - x
        temp = math.ceil(candies / 4)
        print(temp)

