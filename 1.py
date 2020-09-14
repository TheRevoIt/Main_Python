with open('task_1.txt', "w") as f_1:
    while True:
        a = f_1.write(input('Введите строку файла: '))
        if not a:
            break
        f_1.write('\n')
