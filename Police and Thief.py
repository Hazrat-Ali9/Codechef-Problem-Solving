policeman = int(input())
for _ in range(policeman):
    a, b = map(int, input().split())
    temp = abs(a - b)
    print(temp)

