t = int(input()) 

for _ in range(t):
    x, y, z = map(int, input().split())

    if x == y:
        print(z - 1)
        
    elif y // x > z:
        print(0)
    else:
        print(z - (y // x))

