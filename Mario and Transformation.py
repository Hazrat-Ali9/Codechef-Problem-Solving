t = int(input())
while t != 0:
    X = int(input())
    if X % 3 == 0:
        print("NORMAL")
    elif (X + 1) % 3 == 0:
        print("SMALL")
    elif (X + 2) % 3 == 0:
        print("HUGE")
    t -= 1

