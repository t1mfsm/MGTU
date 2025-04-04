import json
import functools
import time
import sys
from random import randint

# Путь к файлу с данными
path = "C:/Users/shaki/OneDrive/Programming/Python/Lab2/data_light.json"

# Загрузка данных из JSON файла
with open(path, encoding='utf-8') as f:
    data = json.load(f)

# Декоратор для печати результатов
def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)
        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)
        return result
    return wrapper

# Контекстный менеджер для засечения времени
class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"time: {elapsed_time}")

# Функция f1 - сортировка и уникальность профессий
@print_result
def f1(data):
    return sorted(set(item['job-name'].lower() for item in data))

# Функция f2 - фильтрация профессий, начинающихся с "программист"
@print_result
def f2(data):
    return list(filter(lambda x: x.startswith('программист'), data))

# Функция f3 - добавление "с опытом Python" к профессиям
@print_result
def f3(data):
    return list(map(lambda x: x + ', с опытом Python', data))

# Функция f4 - генерация зарплат для профессий
@print_result
def f4(data):
    salaries = [f"{item[0]}, зарплата {item[1]} руб." for item in zip(data, (randint(100000, 200000) for _ in range(len(data))))]
    return salaries

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
