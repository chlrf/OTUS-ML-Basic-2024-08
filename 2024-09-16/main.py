from operator import index

print('Домашнее задание от 2024-09-16 - Функции\n')
#  №1
#  Написать функцию, которая будет перводит снейк_кейс в КэмелКейс и наоборот.
#  Функция сама определяет - какой формат ей передали.
#  Можно добавить ключевой аргумент, который будет принудительно возвращать один из форматов.
#  Пример:
#  otus_course -> OtusCourse
#  PythonIsTheBest -> python_is_the_best
print('Задача 1/4: ')

var_name_in = list(input("Введите строку в снейк_кейс или КэмелКейс: "))


def snake_camel(var_name: list):
    if var_name[0].islower():
        var_name[0] = var_name[0].capitalize()
        while '_' in var_name:
            var_name[var_name.index('_') + 1] = var_name[var_name.index('_') + 1].capitalize()
            var_name.remove('_')
    else:
        var_name[0] = var_name[0].lower()
        for i in range(1, len(var_name)):
            if var_name[i].isupper():
                var_name[i] = var_name[i].lower()
                var_name.insert(i, '_')
    return var_name


print(''.join(snake_camel(var_name_in)))


# №2
# Написать функцию проверяющую валидность введенной даты.
# Пример:
# 29.02.2000 -> True
# 29.02.2001 -> False
# 31.04.1962 -> False
print('\nЗадача 2/4: ')

days_in_month = {1: 31,
                 2: [28, 29],
                 3: 31,
                 4: 30,
                 5: 31,
                 6: 30,
                 7: 31,
                 8: 31,
                 9: 30,
                 10: 31,
                 11: 30,
                 12: 31}


def check_leap_year(year):
    if year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
            else:
                return False

def check_date(day, month, year):
    if month not in range(1, 13):
        return False
    else:
        if month != 2:
            if day in range(1, days_in_month[month] + 1):
                return True
            else:
                return False
        else:
            if check_leap_year(year):
                if day in range(1, days_in_month[month][1] + 1):
                    return True
                else:
                    return False
            else:
                if day in range(1, days_in_month[month][0] + 1):
                    return True
                else:
                    return False



while True:
    date = input("Введите дату в формате ЧЧ.ММ.ГГГГ: ")
    date = list(date.split('.'))
    if (date[0].isdigit() and len(date[0]) == 2 and
            date[1].isdigit() and len(date[1]) == 2 and
            date[2].isdigit() and len(date[2]) == 4):

        day, month, year = int(date[0]), int(date[1]), int(date[2])
        print(check_date(day, month, year))
    break


# №3
# Функция проверки на простое число. Простые числа – это такие числа, которые делятся на себя и на единицу.
# Пример:
# 17 -> True
# 20 -> False
# 23 -> True
print('\nЗадача 3/4: ')

from math import sqrt


def is_prime_number(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, round(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


while True:
    num = input("Введите целое положительное число: ")
    if num == '':
        break
    if num.isdigit():
        print(is_prime_number(int(num)))


# №4
# Пользователь в бесконечном цикле вводит данные пользователей: имя, затем фамилию, возраст и ID.
# Ввод продолжается до тех пор, пока не будет введено пустое поле. Пользователи заносятся в словарь,
# где ключ это ID пользователя, а остальные данные записываются в виде кортежа.
# Так же программа должна проверять, что имя и фамилия состоят только из символов и начинаются с большой буквы,
# если не с большой, то заменяет на большую, возраст должен быть числом от 18 до 60, ID - целое число,
# дополненное до 8 знаков незначащими нолями, ID должен быть уникальным
# Дополнительно написать функцию, которая будет выводить полученный словарь в виде таблицы
print('\nЗадача 4/4: ')


def validate_input_data(name, surname, age, user_id):
    if user_id.isdigit() and int(user_id) in [int(key) for key in users.keys()]:
        print("! Пользователь с таким ID уже зарегистрирован")
        return False

    validation_passed = True
    if not (name.isalpha() and surname.isalpha()):
        print("! Ошибка ввода имени")
        validation_passed = False
    if not age.isdigit():
        print("! Ошибка ввода возраста")
        validation_passed = False
    if age.isdigit() and int(age) not in range(18, 61):
        print("! Пользователь должен иметь возраст от 18 до 60 лет")
        validation_passed = False
    if not user_id.isdigit() or len(user_id) > 8:
        print("! Ошибка ввода ID")
        validation_passed = False
    return validation_passed


def print_users_table(users_dict):
    print("\n       Таблица пользователей         ")

    def make_width(string):
        return string.ljust(15, ' ')

    header = ['Имя', 'Фамилия', 'Возраст', 'ID пользователя']
    for item in header:
        print(make_width(item), end=' ')
    print()

    for key in users_dict.keys():
        for value in users_dict[key]:
            print(make_width(str(value)), end=' ')
        print(make_width(key), end=' ')
        print()


users = {}
while True:
    data_in = input("Введите через пробел Имя Фамилию Возраст ID: ")
    if data_in == '':
        break
    data_in = data_in.split(' ')
    name, surname, age, user_id = data_in[0], data_in[1], data_in[2], data_in[3]
    if validate_input_data(name, surname, age, user_id):
        users[user_id.zfill(8)] = name.capitalize(), surname.capitalize(), int(age)

print_users_table(users)
