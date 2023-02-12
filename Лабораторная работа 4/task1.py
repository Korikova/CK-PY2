import doctest


class Cinema:
    def __init__(self, name: str, film_director: str, rating: float):
        """Создание и подготовка к работе объекта "Кинематорграф"
        :param name: название кино
        :param film_director: кинорежиссер
        :param rating: рейтинг(оценка)
        """
        self._name = name
        self._film_director = film_director
        self._rating = rating

    @property
    def name(self):
        return self._name

    @property
    def film_director(self):
        return self._film_director

    @property
    def rating(self):
        return self._rating

    def __str__(self) -> str:
        return f"Название кино: {self.name}. Кинорежиссер: {self.film_director}. Рейтинг(оценка): {self.rating}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: (name={self.name!r}, film_director={self.film_director!r}, " \
               f"rating={self.rating!r})"

    def check_rating(self) -> bool:
        """Функция, которая проверяет фильм/сериал на предмет высокого рейтинга
        Если если рейтинг фильма/сериала >= 7.0, то выведет True, что говорит о достаточно хорошем рейтинге(оценке)
        фильма/сериала
        :return: Покажет хороший ли рейтинг у фильма/сериала
        """
        if self.rating >= 7.0:
            return True
        else:
            return False


class FantasticMovie(Cinema):
    def __init__(self, name: str, film_director: str, rating: float, computer_graphics: str):
        """Создание и подготовка к работе объекта "Фантастический фильм"
        :param name: название кино
        :param film_director: кинорежиссер
        :param computer_graphics: компьютерная графика
        """
        super().__init__(name, film_director, rating)
        self._computer_graphics = computer_graphics

    @property
    def computer_graphics(self):
        return self._computer_graphics

    @computer_graphics.setter
    def computer_graphics(self, new_computer_graphics: str) -> None:
        """Устанавливает вид компьютерной графики"""
        if not isinstance(new_computer_graphics, str):
            raise TypeError("Вид компьютеной графики должен быть типа str")
        self._computer_graphics = new_computer_graphics

    def check_rating(self):
        super_check_rating = super().check_rating()
        return f"{super_check_rating}"

    def __str__(self) -> str:
        return f"Название кино: {self.name}. Кинорежиссер: {self.film_director}. Рейтинг(оценка): {self.rating}. " \
               f"Компьютерная графика: {self.computer_graphics}."


class Serial(Cinema):
    def __init__(self, name: str, film_director: str, rating: float, episodes: int):
        """Создание и подготовка к работе объекта "Сериал"
        :param name: название кино
        :param film_director: кинорежиссер
        :param episodes: количество серий
        """
        super().__init__(name, film_director, rating)
        self._episodes = episodes

    @property
    def episodes(self):
        return self._episodes

    @episodes.setter
    def episodes(self, new_episodes: int) -> None:
        """Устанавливает количество страниц в книге"""
        if not isinstance(new_episodes, int):
            raise TypeError("Количество серий должно быть типа int")
        if new_episodes <= 1:
            raise ValueError("Количество серий не может иметь значение ниже 2")
        self._episodes = new_episodes

    def check_rating(self):
        super().check_rating()
        return f"Первый сезон сериала вышел в 2013 года"

    def __str__(self) -> str:
        return f"Название кино: {self.name}. Кинорежиссер: {self.film_director}. Рейтинг(оценка): {self.rating}. " \
               f"Количество серий: {self.episodes}."


if __name__ == "__main__":
    cinema = Cinema("Скорость", "Ян де Бонт", 7.8)
    print(cinema.name)
    print(cinema.check_rating())
    print(cinema.rating)
    fantastic_movie = FantasticMovie("Аватар", "Джеймс Кэмерон", 8.0, "CGI")
    print(fantastic_movie.check_rating())
    print(fantastic_movie.computer_graphics)
    serial = Serial("Викинги", "Кэтрин Уинник", 8.2, 90)
    print(serial.episodes)
    print(serial.check_rating())
    serial.episodes = 3
    print(serial.episodes)
    doctest.testmod()
    pass
