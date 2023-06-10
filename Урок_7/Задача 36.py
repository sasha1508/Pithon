# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**

# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

import subprocess
import os


subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли

func = input("Введи текст функции: ")
funcName = func.split('(', 1)[0]
argument = func.split('(', 1)[1].split(')', 1)[0]
lfunc = eval(argument)
print(funcName)
print(argument)

def print_operation_table(operation, num_rows=6, num_columns=6):
    arr = list(range(1, num_columns + 1))
    
    print()
    print(arr)
    
    for i in range(num_rows - 1):
        y = i + 2
        print(list(map(lambda x:lfunc(x, y), arr)))

    print()
    
f = locals()[funcName]
f(argument)
