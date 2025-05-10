for i in range(int(input())):
    (W, X, Y, Z) = map(int, input().split(' '))
    if X==W or Y==W or Z==W:
        print("YES")
    elif (X+Y) == W or (X+Z) == W or (Y+Z)==w or (X+Y+Z) ==W:
        print("YES")
    else:
        print("NO")
# Weights