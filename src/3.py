# ----------------------------------------------------
# Заздравных Василий Владимирович
# Группа №41703620
# Зачетная книжка №4170362010
# ----------------------------------------------------
# Лабараторная работа №3
# ----------------------------------------------------
# Вариант №10
# ----------------------------------------------------

import math

print("Задание №1")

""" Разработать интерактивную программу «Quadric Equation» («Квадратное уравнение») для решения квадратных уравнений вида: ax2 + bx + c = 0. Программа должна запрашивать у пользователя соответствующие параметры a, b, с и, в зависимости от вычисленного дискриминанта D, выдавать соответствующий результат. В случае отрицательного дискриминанта программа должна выводить сообщение о том, что действительных корней нет. """

print("Решение квадратного уровнения вида ax2 + bx + c = 0.")

a = float(input("Введите \"a\": "))
b = float(input("Введите \"b\": "))
c = float(input("Введите \"c\": "))

print("a = " + str(a))
print("b = " + str(b))
print("c = " + str(c))

if a != 0 :

    d = b ** 2 - 4 * a * c
    print("d = " + str(d))

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("Найдены два корня")
        print("x1 = " + str(x1))
        print("x2 = " + str(x2))
    else:
        if d == 0:
            x = d / 2 / a
            print("Найден только один корень")
            print("x = " + str(x))
        else:
            print("Корней не найдено")
else:
    print("\a\" не может равняться нулю!")

# Убрать, когда нужно будет показать работу второго задания
exit()

print("Задание №2")


""" 
Вычислить значение y в зависимости от выбранной функции (x), аргумент которой определяется из поставленного условия. Возможные значения функции        (x): 2x, x**2, х/3 (в приложении выбор выполнить с помощью меню). Предусмотреть вывод сообщений, показывающих, при каком условии и с какой функцией производились вычисления у. 
"""

def selectFunc():
    print("Выберите функцию, введя число, где\n1 = 1 - 2x\n2 = 2 - x ^ 2\n3 = 3 - x / 3")
    return int(input())

select = selectFunc()

print("Введите числовые значения для переменных \"d\" \"c\" и \"z\"")
d = float(input("Введите \"d\": "))
c = float(input("Введите \"c\": "))
z = float(input("Введите \"z\": "))

x = 0
if z <= 1:
    x = z ** 2 + 1
else:
    x = z - 1

fx = 0

if select == 1:
    fx = 2 * x
    print("Была выбрана функция №1. 1-2x")
elif select == 2:
    fx = x ** 2
    print("Была выбрана функция №2. 2 - x ^ 2")
elif select == 3:
    fx = fx / 3
    print("Была выбрана функция №3. 3 - x / 3")
else:
    print("\n!!! Функция не выбрана !!!\n")
    selectFunc()

res = (d * fx * math.exp((math.sin(x)) ** 3) + c * math.log(x + 1)) / (x ** (1/2))
print(res)
