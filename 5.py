class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.__class__.__name__}')
class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.__class__.__name__}')
class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.__class__.__name__}')
P = Pen('title1')
Penc = Pencil('title2')
P.draw()
Penc.draw()
