t = int(input())

for _ in range(t):
    a, b, x, y = map(float, input().split())
    climb = a / x
    down = b / y

    if climb == down:
        print("Both")
    elif climb > down:
        print("Chefina")
    else:
        print("Chef")

