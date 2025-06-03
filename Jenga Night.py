m = int(input())
while m != 0:
    N, X = map(int, input().split())
    if X % N == 0:
        print("YES")
    else:
        print("NO")
    m -= 1

