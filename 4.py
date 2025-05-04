def trace_execution(original_function):
    def wrapped(*args, **named_args):
        print(f"Вызов функции '{original_function.__name__}' с параметрами:")
        print(f"Аргументы по позиции: {args}")
        print(f"Аргументы по имени: {named_args}")
        outcome = original_function(*args, **named_args)
        return outcome
    return wrapped

@trace_execution
def compute_rectangle_area(side_a, side_b):
    rectangle_area_value = side_a * side_b
    print(f"Площадь прямоугольника: {rectangle_area_value}")
    return rectangle_area_value

compute_rectangle_area(2, 2)
compute_rectangle_area(side_a=3, side_b=5)

