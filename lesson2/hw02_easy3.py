__author__ = 'Вторушин Марк Викторович'
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# РЕШЕНИЕ ЗАДАЧИ №3
# Импортируем модуль random
import random
# Создаем пустые массивы
a = []
b = []
# Используем цикл для заполнения массива a целыми числами

for i in range(10):
    numbers = round(random.random() * 100)  # Берем целые числа в диапазоне от 0 до 100
    a.append(numbers)

for i in a:
    if (i % 2) == 0:
        x = i / 4
        b.append(x)
    else:
        x = i * 2
        b.append(x)


print("Исходный массив A =", a)
print("B =", b)
