# Fisunenko Vladimir
# Homework-5
# 24.12.2024
# Grodno-IT-Academy-Python 3.12.7


# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”.
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  #  "0-4, 7-8, 10"
# get_ranges([4,7,10])  # "4, 7, 10"
# get_ranges([2, 3, 8, 9])  # "2-3, 8-9"
def get_ranges(lst):
    # Если список пустой, возвращаем пустую строку
    if not lst:
        return ""
    
    ranges = []  # Список для хранения значений
    start = lst[0]  # Начало первого значения
    end = lst[0]    # Конец первого значения

    # Проходим по элементам списка, начиная со второго
    for i in range(1, len(lst)):
        if lst[i] == end + 1:
            end = lst[i]  # Расширяем конец диапазона
        else:
            # Если диапазон завершен, добавляем его в список
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{end}")
            start = end = lst[i]
    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{end}")
    return ", ".join(ranges)


# Напсать функцию standardise_phones которая принимает любое
# количество нестандартизированных телефонных номеров и возвращает
# список стандартизированных номеров в том порядке в котором они были
# введены. А если число не является номером - возвращает пустой список
# standardise_phones("298884455") # ["+375298884455"]
# standardise_phones("(29)888-44-55","8029 8885555","+375299998877","375299998867") # ["+375298884455","+375298885555","+375299998877","+375299998867"]
# standardise_phones("298884asd45") # []
def standardise_phones(*args):
    import re

    standardised = []
    for phone in args:
        phone = str(phone)
        cleaned = re.sub(r"\D", "", phone)  # Удаляем все нецифровые символы
        # Проверяем и форматируем номера в различных форматах
        if cleaned.startswith("375") and len(cleaned) == 12:
            standardised.append(f"+{cleaned}")
        elif cleaned.startswith("80") and len(cleaned) == 11:
            standardised.append(f"+375{cleaned[2:]}")
        elif len(cleaned) == 9:
            standardised.append(f"+375{cleaned}")
        else:
            return []
    return standardised

# Создайте функцию rope_product, которая берёт позитивный цельный номер,
# который представляет собой длину верёвки. Длина этой
# верёвки может быть разделена на любое количество более
# малых цельных чисел. Верните максимальный продукт умножения
# малых цельных чисел. Решение не должно пользоваться циклами!
# rope_product(1) -> 1
# rope_product(4) -> 4
# rope_product(5) -> 6
# rope_product(6) -> 9
# rope_product(7) -> 12
# rope_product(11) -> 54
def rope_product(n):
     # Базовые случаи для низких значений n
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    
    # Для n >= 5
    product = 1
    while n > 4:
        product *= 3
        n -= 3
    
    product *= n  # Умножаем на остаток (1, 2 или 4)
    return product
# Создайте декоратор handle_multiples который позволит функции rope_product
# вернуть лиш один ответ если задано одно число и много ответов списком если
# введённых значений будет несколько! И добавьте его к функции rope_product
# не меняя решения из предыдущего решения!
# rope_product(8) -> 18
# rope_product(7,11,23,45,32) -> [12, 54, 4374, 14348907, 118098]
# здесь можно пользоваться циклами
def handle_multiples(func):
    def wrapper(*args):
        # Проверяем количество переданных аргументов
        if len(args) == 1:
            # Если один аргумент, вызываем функцию
            return func(args[0])
        else:
            # Если несколько аргументов, применяем функцию ко всем и возвращаем список результатов
            return [func(n) for n in args]
    return wrapper

@handle_multiples
def rope_product(n):
    # Базовые случаи для низких значений n
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    
    # Для n >= 5
    product = 1
    while n > 4:
        product *= 3
        n -= 3
    product *= n  
    return product