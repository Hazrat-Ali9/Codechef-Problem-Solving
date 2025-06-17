def power(x, y, MOD=float('inf')):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power((x * x) % MOD, y // 2, MOD) % MOD
    else:
        return (x * power((x * x) % MOD, (y - 1) // 2, MOD)) % MOD

def main():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        if a + c == 180 and b + d == 180:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

