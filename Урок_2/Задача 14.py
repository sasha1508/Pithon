# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import subprocess
import os
import random

subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли

n = int(input("Введи число N: "))

if n < 0:
    print()
    print("Необходимо ввести положительное число число больше нуля!")
    print()
else:
    list_1 = [] # Создание пустого списка
    i = 0
    k = 0
    while k < n:
        k = 2 ** i
        if not k <= n:
            break
        list_1.append(k)
        i = i + 1

    print(list_1)
        
