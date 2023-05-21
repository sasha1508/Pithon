# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


import subprocess
import os

subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли

chislo = int(input("Введи трёхзначное число: "))

if chislo > 99 and chislo < 1000:
    digit1 = chislo % 10
    digit2 = chislo // 10 % 10
    digit3 = chislo // 100 % 10
    sum = digit1 + digit2 + digit3
    print("Сумма цифр: " + str(sum))

else:
    print("Введено не трехзначное число.")
