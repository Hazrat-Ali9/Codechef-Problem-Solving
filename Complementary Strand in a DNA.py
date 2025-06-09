t = int(input())
for _ in range(t):
    n = int(input())
    strand = input()
    complement = ''

    for ch in strand:
        if ch == 'A':
            complement += 'T'
        elif ch == 'T':
            complement += 'A'
        elif ch == 'C':
            complement += 'G'
        else:  # ch == 'G'
            complement += 'C'

    print(complement)

