# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

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
    sum = 0 
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
    for i in money:
        if Ai[i] == x:
            sum += 1

print("Ответ: " + str(sum))