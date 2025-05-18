for _ in range(int(input())):
    a,b,c=map(int, input().split())
    if b*1+c*2>=a:
        print("Qualify")
    else:
        print("NotQualify")
