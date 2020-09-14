with open('task_5.txt', "w") as f_5:
    a = f_5.write(f'{input("Введите числа через пробел: ")}')
with open('task_5.txt', "r") as f_5a:
    content = f_5a.readline()
    suma = 0
    for i, el in enumerate(content.split(' ')):
        suma += int(el)
print(f'Сумма чисел: {suma}')




