m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if (a == 0 and b == 0 and c == 0) or\
       (a == 1 and b == 0 and c == 0) or\
       (b == 1 and a == 0 and c == 0) or\
       (c == 1 and a == 0 and b == 0):
        
        print("Water filling time")

    else:
        print("Not now")

