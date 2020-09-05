def int_func(word):
    word = list(word)
    word[0] = word[0].upper()
    return ''.join(word)

def stroka():
    int_str = input('Введите строку из слов, разделенных пробелами ').split()
    str1 = ''
    for i in int_str:
        str1 += f'{int_func(i)} '
    return f'{str1}'


print(stroka())

