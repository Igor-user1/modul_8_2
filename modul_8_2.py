def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        middle_arithmetic = personal_sum(numbers)[0]/len(numbers)
        return middle_arithmetic
    except ZeroDivisionError:
        return 'Деление на ноль! Ответ: 0'
    except TypeError:
        return 'В numbers записан некорректный тип данных'


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
