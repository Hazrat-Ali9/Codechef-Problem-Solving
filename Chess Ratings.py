def minimum_games_to_reach_rating():
    T = int(input())  
    for _ in range(T):
        X, Y = map(int, input().split())
        diff = Y - X
        games = (diff + 7) // 8  
        print(games)


minimum_games_to_reach_rating()

