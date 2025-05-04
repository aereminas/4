def add_content_to_file(content, file_path):
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content + '\n')

    except Exception as error:
        print(f"Ошибка записи в файл: {error}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            all_lines = file.readlines()

        for index, current_line in enumerate(all_lines):
            if (index + 1) % 2 == 0:
                print(current_line.strip())

    except FileNotFoundError:
        print("Файл не обнаружен.")
    except Exception as error:
        print(f"Ошибка чтения файла: {error}")

add_content_to_file("Новая строка", "data.txt")
