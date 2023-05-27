# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import subprocess
import os
import random

subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли

n = int(input("Введи число N: "))

if n < 1:
    print()
    print("Необходимо ввести число больше нуля!")
    print
else:
    Ai = [] # Создание пустого списка

    money = range(n)
    otvet = 0

    for i in money:
        Ai.append(int(random.random() * 10))

print(Ai)

x = int(input("Введи искомое число X: "))

if n < 1:
    print()
    print("Необходимо ввести число больше нуля!")
    print
else:
    raznost = x
    for i in money:
        if abs(x - Ai[i]) < raznost:
            raznost = abs(x - Ai[i]) 
            otvet = Ai[i]

print("Ответ: " + str(otvet))