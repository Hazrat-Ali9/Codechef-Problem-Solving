def factorial(f):
    if f==0:
        return 1
    elif f==1:
        return 1
    else:
        return f*factorial(f-1)
n=int(input())
for i in range(n):
    num=int(input())
    print(factorial(num))
