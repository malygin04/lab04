# Функция для перевода чисел в словесное представление
def number_to_words(number):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

    if number == 0:
        return "ноль рублей"

    result = ""

    # Проверка ввода чисел
    if number < 0 or number > 100000:
        return "Некорректное число. Введите число от 1 до 100000."

    # Разбиваем число на разряды
    thousands = number // 1000
    hundreds_and_units = number % 1000

 # Функция для обработки тысячи в числе и возвращения ее в текстовое представление
    def process_thousands(number):
        units = ['', 'одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
        tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
                'девяносто']
        hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот',
                    'девятьсот']

        result = ""

        # Обрабатываем сотни
        if number >= 100:
            result += hundreds[number // 100] + " "
            number %= 100

        # Обрабатываем десятки и единицы
        if number >= 20:
            result += tens[number // 10] + " "
            number %= 10
        elif 10 <= number < 20:
            result += teens[number - 10] + " "
            number = 0

# Добавляем правильное окончание для слова тысяча
        if number == 1:
            result += "одна тысяча "
        elif number in [2, 3, 4]:
            result += units[number] + " тысячи "
        else:
            result += units[number] + " тысяч "

        return result

    # Обрабатываем тысячи
    if thousands > 0:
        result += process_thousands(thousands)

    # Обрабатываем сотни и единицы
    result += process_number(hundreds_and_units)

    # Добавляем правильное окончание для валюты
    if number % 10 == 1 and number % 100 != 11:
        result += " рубль"
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        result += " рубля"
    else:
        result += " рублей"

    return result

# Функция для обработки отдельных разрядов числа
def process_number(number):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

    result = ""

    # Обрабатываем сотни
    if number >= 100:
        result += hundreds[number // 100] + " "
        number %= 100

    # Обрабатываем десятки и единицы
    if number >= 20:
        result += tens[number // 10] + " "
        number %= 10
    elif 10 <= number < 20:
        result += teens[number - 10] + " "
        number = 0

    if number > 0:
        result += units[number] + " "

    return result

# Получаем число от пользователя
while True:
    try:
        number = int(input("Введите число от 1 до 100000: "))
        break
    except ValueError:
        print("Некорректный ввод. Попробуйте еще раз.")

# Преобразуем число в слова
words = number_to_words(number)

# Выводим результат на экран
print(words)












