with open('task_3.txt', 'r') as f3:
    content = f3.readlines()
    summa = 0
    for line in content:
        if int(line.split()[1]) < 20000:
            print(f'Сотрудник {line.split()[0]} имеет оклад ниже 20000. Оклад {line.split()[1]}')
        summa += int(line.split()[1])
    print(f'Средний оклад сотрудников {summa/len(content)}')