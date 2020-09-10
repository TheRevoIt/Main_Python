from sys import argv
script_name, hours, hourlyrate, bonus = argv
print((int(hours)*int(hourlyrate))+int(bonus))
