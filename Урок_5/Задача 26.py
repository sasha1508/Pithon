# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

import subprocess
import os

subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли

A = int(input("Введи число A: "))
B = int(input("Введи число B: "))

def stepen(A, B):
    if B == 0: return 1
    elif B == 1: return A
    return stepen(A, B - 1) * A

if A < 0 or B < 0:
    print()
    print("Необходимо ввести неотрицательное число!")
    print
else:
    otvet = stepen(A, B)
    print(otvet)




