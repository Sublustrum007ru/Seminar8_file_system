from print_data import print_file
from num_files import num_files
from clear_console import clear


def choice_number_file():
    clear()
    print_file()
    number = int(input("Выберит файл, с которым Вы хотите работать\n"
                       f"Введите цифру 1 или {num_files()}: "))
    while number < 1 or number > num_files():
        number = int(input("Ошибка!!!\n"
                           f"Введите цифру 1 или {num_files()}: "))
    return number
