def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, (int, float)):
        # Если элемент - число, добавляем его к сумме
        total_sum += data
    elif isinstance(data, str):
        # Если элемент - строка, добавляем её длину к сумме
        total_sum += len(data)
    elif isinstance(data, (list, tuple, set)):
        # Если элемент - список, кортеж или множество, рекурсивно обрабатываем каждый элемент
        for item in data:
            total_sum += calculate_structure_sum(item)
    elif isinstance(data, dict):
        # Если элемент - словарь, обрабатываем ключи и значения рекурсивно
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)

    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)