# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


import subprocess
import os
import random

subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли

n = int(input("Введи количество монеток: "))

if n < 1:
    print()
    print("Необходимо ввести число больше нуля!")
    print
else:
    list_1 = [] # Создание пустого списка

    money = range(n)
    sum = 0 
    otvet = 0

    for i in money:
        list_1.append(int(random.random() * 2))
        sum = sum + list_1[i]

    print()
    print(list_1)
    print('"0" - лежит вверх решкой') 
    print('"1" - лежит вверх гербом') 
    print()

    if sum < (n / 2):
        otvet = sum
    else:
        otvet = n - sum

    print("Количество монеток, которые необходим перевернуть: " + str(otvet))
    print()
