# ----------------------------------------------------
# Заздравных Василий Владимирович
# Группа №41703620
# Зачетная книжка №4170362010
# ----------------------------------------------------
# Лабараторная работа №2
# ----------------------------------------------------
# Вариант №10
# ----------------------------------------------------


import math

print("x = 3.981e-2;\ny = -1.625e3;\nz = 0.512;")

x = 3.981e-2
y = -1.625e3
z = 0.512

a = 2 ** -x * ((x + (abs(y)) ** (1/4)) ** (1/2)) * (math.exp(x - (1 / math.sin(z))))  ** (1/3)
print("Вычисление по формуле даст:\n" + str(a))
