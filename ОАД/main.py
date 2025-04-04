# import pandas as pd

# # Чтение CSV файла и округление столбца
# def ocr(input_file, output_file, column_name):
#     # Чтение данных из файла
#     df = pd.read_csv(input_file)

#     # Берём столбец D (индекс 3) начиная со второй строки (индекс 1)
#     df[column_name] = df[column_name].iloc[1:].round()  # Округляем начиная с 2-й строки

#     # Сохраняем результат в новый файл
#     df.to_csv(output_file, index=False)

#     # Выводим округлённые значения
#     print(df[column_name])

# # Путь к файлу с данными
# input_file = 'checks_iu5_55.xlsx'  # Замените на путь к вашему файлу
# output_file = 'rounded_file.xlsx'  # Замените на путь, куда сохранить результат
# column_name = 'D'  # В столбце D

# # Вызов функции
# ocr(input_file, output_file, column_name)


import pandas as pd

# Чтение CSV файла и округление столбца
def округлить_столбец(input_file, output_file, column_name):
    # Чтение данных из файла с указанием кодировки
    df = pd.read_csv(input_file, encoding='utf-8-sig')  # Используем 'utf-8-sig' или 'ISO-8859-1'

    # Берём столбец D (индекс 3) начиная со второй строки (индекс 1)
    df[column_name] = df[column_name].iloc[1:].round()  # Округляем начиная с 2-й строки

    # Сохраняем результат в новый файл
    df.to_csv(output_file, index=False)

    # Выводим округлённые значения
    print(df[column_name])

# Путь к файлу с данными
input_file = 'checks_iu5_55.xlsx'  # Замените на путь к вашему файлу
output_file = 'rounded_file.xlsx'  # Замените на путь, куда сохранить результат
column_name = 'D'  # В столбце D

# Вызов функции
округлить_столбец(input_file, output_file, column_name)
