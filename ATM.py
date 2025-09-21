x, y = input().split()
x = int(x)         
y = float(y)        

if x % 5 == 0 and x + 0.50 <= y:
    y -= (x + 0.50)

print(f"{y:.2f}")

