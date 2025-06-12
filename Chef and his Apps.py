def solve():
    s, x, y, z = map(int, input().split())
    if z <= s - x - y:
        print(0)
    elif z <= s - min(x, y):
        print(1)
    else:
        print(2)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
