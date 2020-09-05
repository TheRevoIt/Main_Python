def data(name,surname,yearofbirth,email,phonenumber):
    return f"{name} {surname} {yearofbirth} г. {email} {phonenumber}"
print(data(name=input('Введите имя '), surname=input('Введите фамилию '), yearofbirth=int(input('Год рождения ')), email=input('Введите эл. почту '), phonenumber=int(input('Введите номер телефона '))))
