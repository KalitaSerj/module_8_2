def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        total_sum, incorrect_data = personal_sum(numbers)
        if len(numbers) == 0:
            return 0
        else:
            return total_sum / len(numbers)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return 'В numbers записан некорректный тип данных'

print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([]))
print(calculate_average([1, 2, 'a', 4, 5]))