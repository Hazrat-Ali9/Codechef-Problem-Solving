for i in range(int(input())):
    (x, y) = map(int, input().split(' '))
    
    if (x/y)%2 == 0:
        print("Yes")
    else:
        print("No")
