# Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом

def sum_uneven_index(arr):
    res = 0
    for i in range(1, len(arr), 2):
        res += int(arr[i])
    print(res)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def product_pairs(arr):
    res = []
    arr = list(map(int, arr))
    for i in range((len(arr)+1)//2):
        res.append(arr[i]*arr[-1-i])
    print(res)

# Напишите программу, которая найдёт разницу между макс и мин значением дробной части элементов, отличной от 0.


def difference_max_min_fractional(arr):
    res = []
    for i in range(len(arr)):
        if '.' in str(arr[i]):
            res.append(float('0.'+(str(arr[i]).split('.'))[1]))
    print(max(res)-min(res))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


def binar(n):
    s = ''
    while n:
        s += str(n % 2)
        n = n//2
    print(s[::-1])

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n < 0:
        return ((-1)**(-n+1)) * fib(-n)
    return fib(n-1)+fib(n-2)


def list_fib_nega(k):
    res = []
    for i in range(-k, k+1):
        res.append(fib(i))
    print(res)


a = [2, 3, 5, 9, 3]
b = [2, 3, 5, 6]
c = [2, 3, 4, 5, 6]
d = [1.1, 1.2, 3.1, 5, 10.01]
k = 8

# sum_uneven_index(a)
# product_pairs(b)
# product_pairs(c)
# difference_max_min_fractional(d)
# binar(74)
# list_fib_nega(k)
