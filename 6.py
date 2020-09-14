subjects = {}
with open('task_6.txt', "r") as f_6:
    content = f_6.readlines()
    for line in content:
        name = line.split(":")[0]
        numbers = line.split(":")[1]
        num_list ="".join([el for el in numbers if el.isdigit() or el == ' ']).split()
        suma = sum([int(el) for el in num_list])
        subjects[name] = suma
print(subjects)
