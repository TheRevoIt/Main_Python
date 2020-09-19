class Clothes:
    def __init__(self, name):
        self.name = name


class Costume(Clothes):
    def __init__(self, name, height):
        Clothes.__init__(self, name)
        self.height = height

    @property
    def need(self):
        return f'Необходимое количество ткани {2 * self.height + 3}'


class Coat(Clothes):
    def __init__(self, name, size):
        Clothes.__init__(self, name)
        self.size = size

    @property
    def need(self):
        return f'Необходимое количество ткани {self.size / 6.5 + 0.5:.2f}'


costume = Costume('Arms', 10)
coat = Coat('Asos', 15)
print(costume.need)
print(coat.need)