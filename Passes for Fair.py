for _ in range(int(input())):
    N, K = map(int, input().split())

    if K >= N + 1:
        print("YES")
    else:
        print("NO")

