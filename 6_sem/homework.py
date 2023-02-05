# Решение задачния с 4 семинара с List Comprehensions
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint as ri
k = int(input("Enter degree k: "))
coef = [ri(1, 5)] + [ri(0, 5) for i in range(k)]                # генерируем спсиок с k+1 коэфициентами,где при старшем одночлене не равен нулю
peremen = [('x^'+str(i)+' + ') for i in range(k, 1, -1)]+['x']   # создаем список иксов во всех степенях от k до 1
res = ''
for i in range(k):
    if coef[i] != 0:                                        #пропускаем одночлен если коэф равен 0
        if coef[i] == 1:                                   # опускаем коэфициент если он равен 1
            res += peremen[i]
        else:
            res += str(coef[i])+'*'+peremen[i]
res += ' + '+str(coef[-1])                              # дописываем свободный член
print(res)
