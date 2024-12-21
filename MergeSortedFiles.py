import os

def get_file_info(file_path):
    """Считывает файл и возвращает его имя, количество строк и содержимое."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    line_count = sum(1 for _ in content)
    return os.path.basename(file_path), line_count, content

def merge_files(file_paths, output_file):
    """Объединяет файлы в один по указанным правилам."""
    # Считываем информацию обо всех файлах
    file_data = [get_file_info(file_path) for file_path in file_paths]

    # Сортируем файлы по количеству строк
    file_data.sort(key=lambda x: x[1])

    # Записываем данные в результирующий файл
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name, line_count, content in file_data:
            out_file.write(f"{file_name}\n")
            out_file.write(f"{line_count}\n")
            out_file.writelines(content)
            if not content[-1].endswith('\n'):
                out_file.write("\n")

# Пример использования
file_paths = ["1.txt", "2.txt", "3.txt"]  # Список путей к файлам
output_file = "result.txt"  # Имя результирующего файла
merge_files(file_paths, output_file)
