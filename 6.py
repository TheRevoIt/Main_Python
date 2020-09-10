from itertools import count
for el in count(int(input('Введите стартовое значение итератора '))):
    if el >100:
        break
    else:
        print(el)

from itertools import cycle
i = 0
my_list = [1, 4, 5, 65, 1, 34, 2, 1, 4, 5]
for el in cycle(my_list):
    if i > len(my_list)-1:
        break
    else:
        print(el)
        i+=1