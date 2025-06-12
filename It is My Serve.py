def table_tennis(a, b):
    temp = a + b
    turn = (temp // 2) % 2
    return "Alice" if turn == 0 else "Bob"

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(table_tennis(a, b))

# call the function
main()

