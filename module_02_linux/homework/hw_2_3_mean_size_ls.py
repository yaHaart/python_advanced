"""
Напишите функцию, которая будет по output команды ls возвращать средний размер файла в папке.
В качестве аргумента функции должен выступать путь до файла с output команды ls
"""
import os


def get_mean_size(ls_output_path: str) -> float:
    file_list = list()
    with open(ls_output_path, 'r') as output_file:
        temp_file_list = output_file.read().splitlines()
        for file in temp_file_list:
            temp_path = os.path.join('', file)
            file_list.append(os.path.getsize(temp_path))
    return sum(file_list) / len(file_list)


if __name__ == "__main__":
    print(get_mean_size('output.txt'))

# Зачёт!

