from time import sleep
class TrafficLight:

    __colors = {'красный':7, 'желтый':2, 'зеленый':10}

    def running(self):
        for i in iter(self.__colors):
            print(f'Текущий цвет светофора {i}')
            sleep(self.__colors[i])

tr = TrafficLight()
tr.running()