class Road:
    def __init__(self, length, width):
        self.lenght = length
        self.width = width
    def calculations(self, mass, thickness):
        return self.lenght * self.width * mass * thickness
R = Road(20, 5000)
print(R.calculations(25, 5))