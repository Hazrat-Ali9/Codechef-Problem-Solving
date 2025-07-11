cases = int(input())
x = []
y = []

for _ in range(cases):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(cases):
    print(x[i] * y[i])
