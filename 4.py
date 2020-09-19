class Car:
    def __init__(self, speed, color, name, ispolice):
        self.speed = speed
        self.color = color
        self.name = name
        self.ispolice = ispolice

    def go(self, speed):
        print('Машина поехала')
        self.speed = speed

    def stop(self):
        print('Машина остановилась')
        self.speed = 0

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def showspeed(self):
        print(self.speed)


class TownCar(Car):

    def showspeed(self):
        super().showspeed()
        print(f'Превышена скорость' if self.speed > 60 else '')


class SportCar(Car):
    pass


class WorkCar(Car):
    def showspeed(self):
        super().showspeed()
        print(f'Превышена скорость' if self.speed > 40 else '')


class PoliceCar(Car):
    pass


T = TownCar(100, 'blue', 'toyota', False)
T.stop()
T.showspeed()
T.turn('налево')
W = WorkCar(41, 'yellow', 'honda', False)
W.stop()
W.go(41)
W.showspeed()
