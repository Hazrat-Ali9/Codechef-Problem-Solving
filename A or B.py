T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    score_A_first = max(0, 500 - 2 * X) + max(0, 1000 - 4 * (X + Y))
    score_B_first = max(0, 1000 - 4 * Y) + max(0, 500 - 2 * (X + Y))
    print(max(score_A_first, score_B_first))

