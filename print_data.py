from clear_console import clear
from num_files import num_files
def print_file():
    clear()
    for i in range(1, num_files() + 1):
        with open(f'db/data_{i}.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
        print(f"Вывод данных из {i}-ого файла:\n"
              f"{''.join(data)}")
        print()
