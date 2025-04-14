for i in range(int(input())):
    m = input()
    n = m.split()
    avg = float((int(n[0])+int(n[1]))/2)
    if avg > int(n[2]):
        print("YES")
    else:
        print("NO")
