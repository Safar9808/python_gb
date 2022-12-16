# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

def sumDigits(x):
    s = x.split(',')
    res = 0
    for i in s:
        for j in range(len(i)):
            res = res+int(i[j])
    return res


a = input('Enter number: ')
print(sumDigits(a))

# Задайте список из n чисел последовательности (1 + 1/n)**n,
# выведеите его на экран, а так же сумму элементов списка.


def second_wondefrul_limit(n):
    return [round((1+1/i)**i, 3) for i in range(1,n+1)]

b = int(input('Enter number: '))
print(second_wondefrul_limit(b), sum(second_wondefrul_limit(b)))

# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE

from random import randint
def shuffling(arg):
    print(arg)
    for x in range(100):
        i=randint(0, len(arg)-1)
        j=randint(0, len(arg)-1)
        arg[i], arg[j] = arg[j], arg[i]
    print(arg)

a = input('Enter the list items separated by a space: ').split(' ')
shuffling(a)