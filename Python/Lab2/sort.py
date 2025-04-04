data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    print(data)

    # Без использования lambda-функции
    result = sorted(data, key=abs, reverse=True)
    print(result)

    # С использованием lambda-функции
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)
