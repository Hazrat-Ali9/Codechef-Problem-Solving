def check_qualification(score):
    cricket_world_up = "Yes" if score >= 12 else "No"
    print(cricket_world_up)

team_score = int(input())
check_qualification(team_score)

