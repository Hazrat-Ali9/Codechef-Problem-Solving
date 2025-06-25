T = int(input())
for _ in range(T):
    N = int(input())
   
    if N < 2:
        print(0)
    else:
        count = 1 + (N - 2) // 7
        print(count)

