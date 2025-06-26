R, O, C = map(int, input().split())

remaining_overs = 20 
max_possible_score = C + remaining_overs * 36

if max_possible_score > R:
    print("YES")
else:
    print("NO")

