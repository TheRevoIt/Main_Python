def strsum():
    sum = 0
    while True:
        string = input('Введите строку чисел, разделенных пробелом ').split()
        for n, i in enumerate(string, 1):
            if i.upper() == 'Q':
                return f' Сумма - {sum}', 'Введен стоп - символ'
            sum += int(i)
        print(sum)
        if input('Для выхода из программы нажмите q, для продолжения - Enter:').upper() == 'Q':

            break
    return f' Сумма - {sum}', 'Выполнение прекращено'


print(strsum())