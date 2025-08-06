t = int(input())

for _ in range(t):
    the_array = list(map(int, input().split()))
    the_array.sort()
    print(the_array[1])

