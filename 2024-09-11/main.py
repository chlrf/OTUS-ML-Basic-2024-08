
print('Домашнее задание от 2024-09-11')
# №1
# Пользователь вводит целое число, программа складывает все цифры числа
# с полученным числом - то же самое и так до тех пор, пока не получится однозначное число.
# Пример:
# 545 -> 5
# 12345 -> 6

print("Задача 1/5")

while True:
    number = input("Введите число: ")
    if number.isdigit() and number[0] != '0':

        if len(number) == 1:
            print(number)
        else:
            while len(str(number)) > 1:
                sum_ = 0
                for i in range(len(number)):
                    sum_ += int(number[i])
                number = str(sum_)
            print(number)
        break

# №2
# Кинотеатр. Дан список списков, каждый вложенный список состоит из 1 и 0,
# Количество вложенных списков - количество рядов. Пользователь вводит сколько билетов ему требуется.
# Программа должна найти ряд, где можно приобрести нужно количество билетов (места должны быть рядом).
# Если таких рядов несколько, то ближайший к экрану (ближайшим считается нулевой ряд).
# Ели таких мест нет, то вывести False
# Пример:
# [[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]], 2 -> 1
# [[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]], 2 -> False

print("\nЗадача 2/5")

hall = [[0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]]
print(hall)

num_tickets = int(input("Введите количество билетов: "))
str_to_find = '0, ' * num_tickets
str_to_find = str_to_find[:-2]

flag = True
for i in range(len(hall)):
    seats_in_row = str(hall[i])
    if str_to_find in seats_in_row:
        print(i)
        flag = False
        break
if flag:
    print(False)

# №3
# Написать упрощенную версию алгоритма RLE. Алгоритм RLE объединяет подряд идущие символы в коэффициент и символ.
# Пример:
# aaabbbbccccc -> 3a4b5c
# asssdddsssddd -> 1a3s3d3s3d
# abcba -> 1a1b1c1b1a

print("\nЗадача 3/5")

string = input("Введите строку: ")
answer = str()

count = 1
for i in range(len(string)):
    if i < len(string) - 1:
        if string[i] == string[i + 1]:
            count += 1
            if i + 1 == len(string) - 1:
                answer += (str(count) + string[i])
        else:
            answer += (str(count) + string[i])
            count = 1
            if i + 1 == len(string) - 1:
                answer += (str(count) + string[i + 1])

print(answer)

# №4
# Шифр Цезаря. Пользователь вводит строку и ключ шифра,
# программа должна вывести зашифрованную строку (со сдвигом по ключу).
# Сдвиг циклический. Используем только латинский алфавит, пробелы не шифруются.
# Пример:
# Dog, 2 -> Fqi
# Zak zak, 3 -> Cdn cdn
# Python is the BEST, 5 -> Udymts nx ymj GJXY

print("\nЗадача 4/5")

input_from_user = input("Введите фразу и число: ")
input_from_user = input_from_user.split(', ')

phrase = list(input_from_user[0])
shift = int(input_from_user[1])
for i in range(len(phrase)):
    if phrase[i].islower():
        phrase[i] = chr(ord('a') + (ord(phrase[i]) + shift - ord('a')) % 26)
    if phrase[i].isupper():
        phrase[i] = chr(ord('A') + (ord(phrase[i]) + shift - ord('A')) % 26)

for symbol in phrase:
    print(symbol, end='')
# break


# №5
# Табель успеваемости. Пользователь в бесконечном цикле (пока не будет введена пустая строка) вводит строки вида:
# 'название предмета' 'фамилия ученика' 'оценка'. После окончания ввода программа выводит в консоль
# Название предмета, далее список учеников и все их оценки в виде таблицы
#
# Математика Иванов 5
# Математика Иванов 4
# Литература Иванов 3
# Математика Петров 5
# Литература Сидоров 3
# Литература Петров 5
# Литература Иванов 4
# Математика Сидоров 3
# Математика Петров 5
#
# Математика
# Иванов 5 4
# Петров 5 5
# Сидоров 3
#
# Литература
# Иванов 3 4
# Сидоров 3
# Петров 5

print("\n\nЗадача 5/5")

disciplines = dict()

# Считываем данные и сохраняем их в словарь {Предмет: (фамилия, оценка)}
while True:
    data = input('Введите название предмета фамилию оценку: ')
    if data == '':
        break
    data = data.split(" ")
    if data[0] not in disciplines.keys():
        disciplines[data[0]] = [(data[1], data[2])]
    else:
        disciplines[data[0]].append((data[1], data[2]))

# Печатаем название предмета и создаем словарь {фамилия: оценки} для данного предмета
for discipline in disciplines.keys():
    print(discipline)
    grade_book = dict()
    for student_record in disciplines[discipline]:
        if student_record[0] not in grade_book.keys():
            grade_book[student_record[0]] = [student_record[1]]
        else:
            grade_book[student_record[0]].append(student_record[1])

    # Печатаем фамилию и оценки по данному предмету
    for student in grade_book:
        print(student, end=' ')
        for score in grade_book[student]:
            print(score, end=' ')
        print()
    print()
