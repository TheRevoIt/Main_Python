def my_func(x,y):
    result = 1
    for i in range(y):
        result *= 1 / x
    return 1/x ** y, result
x = float(input('Введите действительное положительное число '))
y = int(input('Введите целое отрицательное число(по модулю) '))
print(f'{my_func(x,y)[0]} {my_func(x,y)[1]}')
