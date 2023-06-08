# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import subprocess
import os
import random

subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли

n = int(input("Введи количество элементов массива: "))

if n < 1:
    print()
    print("Необходимо ввести число больше нуля!")
    print
else:
    Ai = [] # Создание пустого списка
    otvet = []

    s = 5  # начало диапазона
    f = 9  # конец диапазона 

    for i in range(n):
        Ai.append(int(random.random() * 10))

    for i in range(n):
        if Ai[i] > s and Ai[i] < f:
            otvet.append(i)

    print(Ai)
    print(otvet)
    