t = int(input())
while t != 0:
    a, b, c, d = map(int, input().split())
    maximise1 = max(a, b)
    maximise2 = max(c, d)
    print(maximise1 + maximise2)
    t -= 1

