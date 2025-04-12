m = int(input())
for i in range(m):
    rev = 0
    number = int(input())
    while(number):
        remainder = number%10
        rev =rev*10+remainder
        number = int(number/10)
    print(rev)
