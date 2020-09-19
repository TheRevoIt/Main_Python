class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        if sub > 0:
            return Cell(sub)
        else:
            return 'Это сделать невозможно'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def __str__(self):
        return str(self.quantity)

    def make_order(self, row):
        if row > self.quantity:
            print(f'{"*" * self.quantity}')
        n = 0
        for i in range(self.quantity//row + 1):
            if self.quantity - n < row:
                print(f'{"*" * (self.quantity - n)}')
                return ''
            print(f'{"*" * row}')
            n += row
        return ''


a = Cell(15)
b = Cell(10)

print(a - b)
print(b - a)
print(a*b)
print(a+b)
print(a/b)
print(a.make_order(4))
