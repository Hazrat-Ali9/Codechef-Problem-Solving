import math

def solve():
    
    T = int(input())

    
    for _ in range(T):
        X, Y, R = map(int, input().split())
        
        
        endless_appertizers = R // 30
        
       
        mozzarella_sticks = X + endless_appertizers
        
       
        max_plates = math.ceil(mozzarella_sticks / Y)
        
        
        print(int(max_plates))


solve()

