""" 
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной 
"""


# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных



# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines() # разделителей не будет
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
# print(line)
# data.close()

import subprocess
import os


def selectAllReadPhoneNumber ():
    phoneBook = readData('C:/Users/sasha/OneDrive/Рабочий стол/Pithon/Урок_8/phonebook.txt')
    for i in phoneBook:
        print (i)
def selectSomethingReadPhoneNumber ():
    print ("Выбран пункт 2")

def readData (fileName):               # чтение файла
    with open (fileName) as f:
        phoneBook = []
        for line in f:
            phoneBook.append(line.split(','))
    return phoneBook

def writeData (fileName, phoneBook):  # добавляем строку в конец файла
    with open (fileName, 'w') as f:
        for i in phoneBook:
            print (i)
            f.write (','.join(i))
            
        print ("Файл сохранён.")

def addPerson ():             # добавление нового абонента
    phoneBook = readData('C:/Users/sasha/OneDrive/Рабочий стол/Pithon/Урок_8/phonebook.txt')
    print ("Введи данные:")
    number = str(len(phoneBook) + 1)
    surname = str(input("Введи фамилию: "))
    nameFirst = str(input("Введи имя: "))
    nameSecond = str(input("Введи отчество: "))
    phoneNumber = str(input("Введи номер телефона: "))
    phoneBook.append([number, surname, nameFirst, nameSecond, phoneNumber])
    print (phoneBook)
    writeData('C:/Users/sasha/OneDrive/Рабочий стол/Pithon/Урок_8/phonebook.txt', phoneBook)

def reWritePerson ():             # добавление нового абонента
    phoneBook = readData('C:/Users/sasha/OneDrive/Рабочий стол/Pithon/Урок_8/phonebook.txt')
    numberStroki = int(input("Введи номер перезаписываемой строки: "))
    print ("Введи данные:")
    number = str(len(phoneBook))
    surname = str(input("Введи фамилию: "))
    nameFirst = str(input("Введи имя: "))
    nameSecond = str(input("Введи отчество: "))
    phoneNumber = str(input("Введи номер телефона: "))
    phoneBook[numberStroki - 1] = [str(numberStroki), surname, nameFirst, nameSecond, phoneNumber + "\n"]
    print (phoneBook)
    writeData('C:/Users/sasha/OneDrive/Рабочий стол/Pithon/Урок_8/phonebook.txt', phoneBook)

def delPerson():
    number = int(input("Введи номер удаляемой строки: "))
    phoneBook = readData('C:/Users/sasha/OneDrive/Рабочий стол/Pithon/Урок_8/phonebook.txt')
    print('Строка "' + str(number) + '" удалена')
    phoneBook.pop(number - 1)
    writeData('C:/Users/sasha/OneDrive/Рабочий стол/Pithon/Урок_8/phonebook.txt', phoneBook)

def clearConsol():
    subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли
    print ('''ПРИВЕТ, ПОЛЬЗОВАТЕЛЬ 
         [1] -- нажми, чтобы ПОКАЗАТЬ ВСЁ
         [2] -- нажми, чтобы ВЫБРАТЬ 
         [3] -- нажми, чтобы ДОБАВИТЬ ДАННЫЕ
         [4] -- нажми, чтобы УДАЛИТЬ ДАННЫЕ
         [5] -- нажми, чтобы ИЗМЕНИТЬ ДАННЫЕ''')
    

clearConsol()

while True:

    enteredNum = int(input())
    # try:
    if (enteredNum == 1):
        clearConsol()
        selectAllReadPhoneNumber()
    elif (enteredNum == 2):
        clearConsol()
        selectSomethingReadPhoneNumber()
        phoneBook = readData('C:/Users/sasha/OneDrive/Рабочий стол/Pithon/Урок_8/phonebook.txt')
        phoneBook.append(['5', 'H', 'R', 'T', '123\n'])
        writeData ('C:/Users/sasha/OneDrive/Рабочий стол/Pithon/Урок_8/phonebook.txt', phoneBook)
    elif (enteredNum == 3):
        clearConsol()
        addPerson()   
    elif (enteredNum == 4):
        clearConsol()
        selectAllReadPhoneNumber()
        delPerson()   
    elif (enteredNum == 5):
        clearConsol()
        selectAllReadPhoneNumber()
        reWritePerson()      
    else:
        clearConsol()
        print("Введён неправильный номер. Попробуй снова")
        break
    # except:
    #     print ("You entered something, but it's not number")




