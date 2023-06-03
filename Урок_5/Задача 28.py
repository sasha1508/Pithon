# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

import subprocess
import os

subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли

A = int(input("Введи число A: "))
B = int(input("Введи число B: "))

def sum(A, B):
    if B == 0: return A
    elif B == 1: return A + 1
    return sum(A, B - 1) + 1

if A < 0 or B < 0:
    print()
    print("Необходимо ввести неотрицательное число!")
    print
else:
    otvet = sum(A, B)
    print(otvet)