turboDefaultSpeed = 120


class Turbo:
    def speedCheck(speedValue):
        return speedValue * turboDefaultSpeed
    

inputSpeed = int(input("Speed? "))
print(Turbo.speedCheck(inputSpeed))