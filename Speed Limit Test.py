for _ in range(int(input())):
    x,y,z,a=map(int, input().split())
    bob=z/a
    alice=x/y
    if bob > alice:
        print("Bob")
    elif bob<alice:
        print("Alice")
    else:
        print("Equal")
