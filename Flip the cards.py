for _ in range(int(input())):
    x,y=map(int, input().split(' '))
    if x==y or y==0:
        print('0')
    elif x-y > int(x/2):
        print(y)
    else:
        print(x-y)
