import math

T = int(input())
for _ in range(T):
    X, N = map(int, input().split())
    passengers = X * 100
    if passengers >= N:
        print(0)
    else:
        airline = N - passengers
        destination = (airline + 99) // 100  
        print(destination)
