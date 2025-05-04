import math

powered_numbers = [number ** 2 for number in range(1, 11)]
print(f"Квадраты первых десяти натуральных чисел: {powered_numbers}")

weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
weekday_mapping = {weekday: index + 1 for index, weekday in enumerate(weekdays)}
print(f"Соответствие дней недели и их номеров: {weekday_mapping}")

frameworks = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
unique_frameworks = {fw.lower() for fw in frameworks}
print(f"Уникальные теги библиотек в нижнем регистре: {unique_frameworks}")

values = [1, 3, 4, 87, 98, 15, 7, 4]
even_values = [val for val in values if val % 2 == 0]
print(f"Список парных чисел: {even_values}")

custom_factorial_mapping = {i: math.factorial(i) for i in range(1, 6)}
print(f"Соответствие чисел от 1 до 5 и их факториалов: {custom_factorial_mapping}")
