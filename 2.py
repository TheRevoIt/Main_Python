with open('task_2.txt', 'r') as f_2:
    contents = f_2.readlines()
    print(f'Число строк в файле:{len(contents)}')
    for string in contents:
        print(f'Содержимое строки: {string} Длина строки: {len(string)}')
