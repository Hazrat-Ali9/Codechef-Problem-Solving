seat = int(input())
for _ in range(seat):
    bus = int(input())
    if  bus<= 10:
        print("Lower Double")
    elif bus <= 15:
        print("Lower Single")
    elif bus <= 25:
        print("Upper Double")
    else:
        print("Upper Single")

