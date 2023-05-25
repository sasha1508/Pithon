# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

import subprocess
import os

reshenie = False
x1 = 0
x2 = 0

subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли

s = int(input('Введи сумму "X" и "Y": '))
p = int(input('Введи произведение "X" и "Y": '))

if (s > 2000) or (p > 1000000) or (s < 2) or (p < 1):
    reshenie = False
    print("Такого быть не может!")
else:
    d = s * s - 4 * p
    if d >= 0:
        x1 = (s + (d ** 0.5)) / 2
        x2 = (s - (d ** 0.5)) / 2
        if (x1 < 1) or (x1 % 1 > 0) or (x2 < 1) or (x2 % 1 > 0):
            reshenie = False
        else:
            reshenie = True
            x1 = int(x1)
            x2 = int(x2)
    else:
        reshenie = False      

if reshenie:
    print()
    print("X: " + str(x1))
    print("Y: " + str(x2))
    print() 
else:
    print("Решения нет :-(")