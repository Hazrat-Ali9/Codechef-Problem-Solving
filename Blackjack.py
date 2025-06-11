def get_required_no(a, b):
    remain = 21 - (a + b)
    return remain if remain <= 10 else -1

def main():
    cases = int(input())
    a = []
    b = []

    for _ in range(cases):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)

    for i in range(cases):
        print(get_required_no(a[i], b[i]))

main()

