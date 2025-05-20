for _ in range(int(input())):
    r1,r2,r3,r4 = map(int, input().split(' '))
    
    if r1 == 1 or r2 == 1 or r3==1 or r4 == 1:
        print("OUT")
    else:
        print('IN')
        
