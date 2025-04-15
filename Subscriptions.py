import math
for _ in range(int(input())):
    m,n=map( int, input().split())
    print(math.ceil(m/6)*n)
