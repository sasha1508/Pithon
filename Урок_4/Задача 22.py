# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import subprocess
import os

subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли

n = int(input("Введи число N: "))
m = int(input("Введи число M: "))

if n < 1 or m < 1:
    print()
    print("Необходимо ввести число больше нуля!")
    print
else:
    print()
    array1 = []
    for i in range(n):
        array1.append(int(input("Введи число " + str(i + 1) + " первого множества: ")))
    print()
    array2 = []
    for i in range(m):
        array2.append(int(input("Введи число " + str(i + 1) + " второго множества: ")))
    print()
    array11 = set(array1)
    array21 = set(array2)
    arrays = sorted(array11 & array21)
    print(arrays)