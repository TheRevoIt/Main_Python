import json
with open('task_7.txt', "r", encoding='UTF-8') as f8:
    dict_profit = {}
    dict_average = {}
    suma = 0
    counter = 0
    for line in f8:
        name, owner, income, loses = line.split()
        profit = int(income) - int(loses)
        dict_profit[name] = profit
        counter += 1
        suma += profit if profit > 0 else 0
dict_average['average_profit'] = suma/counter
list = [dict_profit, dict_average]
with open("my_file.json", "w") as write_f:
    json.dump(list, write_f)
