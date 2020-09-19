class Worker:
    _income = {'worker1': {'wage': 1000, 'bonus': 500},
              'worker2': {'wage': 1500, 'bonus': 500}}
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{Worker._income[self.position]["wage"]+Worker._income[self.position]["bonus"]}')


pos = Position('Ivan', 'Petrov', 'worker2')
pos.get_full_name()
pos.get_total_income()
