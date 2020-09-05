def my_func():
    list = [int(input('Введите первое число ')), int(input('Введите второе число ')), int(input('Введите третье число '))]
    m = min(list)
    list.remove(m)
    return sum(list)
print(my_func())
