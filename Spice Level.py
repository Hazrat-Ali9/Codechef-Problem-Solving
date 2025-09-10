t = int(input())

for _ in range(t):
    x = int(input())
    if x < 4:
        print("MILD")
    elif 4 <= x < 7:
        print("MEDIUM")
    else:  
        print("HOT")

