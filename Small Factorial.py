m = int(input())
for i in range(m):
    fact = 1
    number = int(input())
    for j in range(1,number+1):
        fact *= j

    print(fact)
