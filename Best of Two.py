T = int(input())

for _ in range(T):
    rolls = list(map(int, input().split()))
    alice = sorted(rolls[:3], reverse=True)
    bob = sorted(rolls[3:], reverse=True)

    alice_score = alice[0] + alice[1]
    bob_score = bob[0] + bob[1]

    if alice_score > bob_score:
        print("Alice")
    elif bob_score > alice_score:
        print("Bob")
    else:
        print("Tie")

