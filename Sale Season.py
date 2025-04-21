for _ in range(int(input())):
    m = int(input())
    if m<=100:
        print(m)
    elif m<=1000:
        print(m-25)
    elif m<=5000:
        print(m-100)
    else:
        print(m-500)

