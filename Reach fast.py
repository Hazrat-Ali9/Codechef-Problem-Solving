import math

t = int(input())
while t != 0:
    x, y, k = map(int, input().split())
    val = abs(y - x)
    res = math.ceil(val / k)
    print(int(res))
    t -= 1

