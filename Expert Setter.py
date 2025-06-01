t = int(input())
while t != 0:
    a, b = map(int, input().split())
    temp = (b * 100) //a
    if temp >= 50:
        print("YES")
    else:
        print("NO")
    t -= 1

