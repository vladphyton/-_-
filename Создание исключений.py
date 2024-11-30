class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers


        if not self.__is_valid_vin(vin):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not self.__is_valid_numbers(numbers):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):  # Проверка на тип данных
            raise IncorrectVinNumber('Некорректный тип vin номер')

        if vin_number < 1000000 or vin_number > 9999999:  # Проверка диапазона
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):  # Проверка на строку
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

        if len(numbers) != 6:  # Проверка длины строки
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')


