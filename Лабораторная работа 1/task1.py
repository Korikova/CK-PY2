import doctest


class Boat:
    def __init__(self, max_capacity_volume: (int, float), occupied_volume: (int, float)):
        """
    Создание и подготовка к работе объекта "Лодка"
    :param max_capacity_volume: максильная грузоподъемность лодки в кг
    :param occupied_volume: заполненный объем лодки в кг
        """
        if not isinstance(max_capacity_volume, (int, float)):
            raise TypeError("Максимальная грузоподъемность лодки должна быть типа int или float")
        if not max_capacity_volume > 0:
            raise ValueError("Максимальная грузоподъемность лодки должна быть положительным числом")
        self.max_capacity_volume = max_capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество груза должно быть типа int или float")
        if not occupied_volume > 0:
            raise ValueError("Количество груза должно иметь положительное значение")
        if occupied_volume > max_capacity_volume:
            raise ValueError("Превышение максильной грузоподъемности лодки")
        self.occupied_volume = occupied_volume

    def add_cargo_to_boat(self, cargo: (int, float)) -> None:
        """
    Добавление в лодку дополнительный груз
    :param cargo: груз
    :raise ValueError: Если вес груза, котрый погружают в лодку превышает свободное место, то вызываем ошибку
        """
    def ready_to_depart(self) -> bool:
        """
    Функция которая проверяет готовность лодки к отправлению
    Если лодка максимально загружена, то она может отправляться в путь
    :return: Готова ли лодка к отправлению
        """


class WashingMachine:
    def __init__(self, width_wm: (int, float), length_wm: (int, float), width_space: (int, float),
                 length_space: (int, float)):
        """
    Создание и подготовка к работе объекта "Стиральная машина"

    :param width_wm: ширина стиральной машины
    :param length_wm: длина стиральной машины
    :param width_space: ширина допустимого расстояния
    :param length_space: длина допустимого расстояния
        """

        if not isinstance(width_wm, (int, float)):
            raise TypeError("Ширина стильной машины должна быть типа int или float")
        if not width_wm > 0:
            raise ValueError("Ширина стиральной машины должна быть положительным числом")
        self.width_wm = width_wm

        if not isinstance(length_wm, (int, float)):
            raise TypeError("Длина стильной машины должна быть типа int или float")
        if not length_wm > 0:
            raise ValueError("Длина стиральной машины должна быть положительным числом")
        self.length_wm = length_wm

        if not isinstance(width_space, (int, float)):
            raise TypeError("Ширина допустимого расстояния должна быть типа int или float")
        if not width_space > 0:
            raise ValueError("Ширина допустимого расстояния должна быть положительным числом")
        self.width_space = width_space

        if not isinstance(length_space, (int, float)):
            raise TypeError("Длина допустимого расстояния должна быть типа int или float")
        if not length_space > 0:
            raise ValueError("Длина допустимого расстояния должна быть положительным числом")
        self.length_space = length_space

    def checking_for_width(self) -> bool:
        """
    Функция проверяет, является ли ширина стиральной машины допустимой для заданного расстояния
    :return: Входит ли ширина стиральной машины в заданное расстояние
    :raise ValueError: Если ширина стиральной машины больше ширины допустимого расстояния, то вызываем ошибку
        """

    def checking_for_length(self) -> bool:
        """
    Функция проверяет, является ли длина стиральной машины допустимой для заданного расстояния
    :return: Входит ли длина стиральной машины в заданное расстояние
    :raise ValueError: Если длина стиральной машины больше длины допустимого расстояния, то вызываем ошибку
        """


class License:
    def __init__(self, surname: str, age: int, acceptable_age: int(16)):
        """
    Создание и подготовка к работе объекта "Права на машину"
    :param surname: Фамилия
    :param age: Возраст
    :param acceptable_age: Приемлемый возраст
        """
        if not isinstance(surname, str):
            raise TypeError("Фамилия должна быть типа str")
        self.surname = surname
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if not age > 0:
            raise ValueError("Возраст не может иметь отрицательное значение")
        self.age = age
        if not isinstance(acceptable_age, int):
            raise TypeError("Приемлемый возраст должен быть типа int")
        if not acceptable_age > 0:
            raise ValueError("Примлемый возраст не может иметь отрицательное значение")
        self.acceptable_age = acceptable_age

    def can_drive(self) -> bool:
        """
    Функция проверят достиг ли человек приемлемого возраста для допуска к обучению
    :return: Достиг ли человек приемлемого возраста для обучения на права
        """
    def time(self):
        """
    Функция проверяет сколько времени (лет) осталось до достижения приемлемого возраста
    :return: Количество лет до достижения приемлемого возраста
    :raise ValueError: Если возраст больше примлемого, то вызываем ошибку
        """


if __name__ == "__main__":
    boat = Boat(100, 50)
    boat.ready_to_depart()
    boat.add_cargo_to_boat(30)
    washing_machine = WashingMachine(5, 10, 6, 12)
    washing_machine.checking_for_width()
    washing_machine.checking_for_length()
    license_ = License("Иванов", 15, 16)
    license_.can_drive()
    license_.time()
    doctest.testmod()
    pass
