from return_data_file import data_file
from selection_row import selection_row


def copy_row():
    ## Выбираем файл от куда будем копировать запись
    from_data, from_nf = data_file()
    ## Посчитали сколичество строк в выбранном файле
    from_count_rows = len(from_data)
    ## Выбираем строку которую будем копировать
    from_row = selection_row(from_count_rows) - 1
    ## Выбираем файл куда будем копировать
    to_data, to_nf = data_file()
    ## Посчитали количесвто строк в файле куда будем копировать
    to_row = len(to_data)
    ## Преобразовали выбранную строку в список
    to_data = from_data[from_row].split(";")
    to_data[0] = to_row + 1
    new_to_data = ";".join(str(i) for i in to_data)
    with open(f'db/data_{to_nf}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{new_to_data}')
    print("Данные успешно записаны!")