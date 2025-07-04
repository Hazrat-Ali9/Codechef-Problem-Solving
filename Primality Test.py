import sys
input = sys.stdin.read


TOT = 10**5


is_prime = [True] * (TOT + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(TOT**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, TOT + 1, i):
            is_prime[j] = False


data = input().split()
t = int(data[0])
numbers = list(map(int, data[1:t+1]))


for n in numbers:
    print("yes" if is_prime[n] else "no")

