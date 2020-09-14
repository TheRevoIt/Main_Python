numbers = {'One': 'Один','Two': 'Два','Three': 'Три','Four': 'Четыре'}
with open('task_4.txt', 'r') as f4:
    with open('task_4a.txt', 'w') as f4a:
        content = f4.readlines()
        for line in content:
            list = line.split(" - ")
            print(list)
            f4a.write(f'{numbers[list[0]]} - {list[1][:1]}'"\n")




