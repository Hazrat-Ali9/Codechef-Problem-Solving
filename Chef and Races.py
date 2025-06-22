t = int(input())

for _ in range(t):
    x, y, a, b = map(int, input().split())
    chef_races = {x, y}
    rival_races = {a, b}
    
    
    wins = len(chef_races - rival_races)
    print(wins)

