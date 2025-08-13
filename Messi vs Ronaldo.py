A, B, X, Y = map(int, input().split())

messi_points = A * 2 + B
ronaldo_points = X * 2 + Y


if messi_points > ronaldo_points:
    print("Messi")
elif messi_points < ronaldo_points:
    print("Ronaldo")
else:
    print("Equal")

