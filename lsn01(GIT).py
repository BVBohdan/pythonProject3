# задание 1.0
total = 44
rez = (0.8*total)
print('Для успешного окончания курса надо сдать', rez, 'домашек.')

# задание Есть координаты (переменные) x1, y1 и x2, y2 рассчитайте и выведите расстояние между точками.
x1, x2, y1, y2 = 2, -1, 3, 7
dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print(dist)

# задание Создайте переменные Высоты ширины и глубины для прямоугольника
h = 6  # высота
w = 9  # ширина
d = 12  # глубина
s = ((h**2 + w**2)**(0.5))*d   # площадь диагонального сечения прямоугольного параллелепипеда
s_shifer = 3*4  # площадь куска шифера
cost_shifer = 600  # стоимость куска шифера
right_amount = s // s_shifer  # необходимое колличество шифера
general_cost = right_amount*cost_shifer  # общая стоимость (сумма)
remains = (s / s_shifer) - (s // s_shifer)  # остатки шифера
print(right_amount)
print(general_cost)
print(remains)

# Отредактируйте код чтобы выполнялись ассерт инструкции. (потребуется знание строковых функций.)
# 1
var1 = 'pyThoN'
var1 = var1.lower()
var1 = var1.capitalize()
var1 = var1.upper()
var1 = var1.lower()
print(var1)

# Сделайте чтобы он выводил 'Привіт Остап' еще тремя способами форматирования.
name = 'Остап'
print(f"Привіт {name}")
print('Привіт {}'.format(name))
print('Привіт %s' % name)

# Задача Почините код
price = 12
weight = 3.4121
rez = weight * price
print(round(rez, 2))

# Задача Используя форматирование и черную магию заставьте этот код выполниться без ошибок.


# Задача Используя слайсы, конкатенацию (обьединение) и смекалку заставьте код работать


# Задача Поменяйте местами значения в переменных
a = 10
b = 55
a, b = b, a
print (a, b)