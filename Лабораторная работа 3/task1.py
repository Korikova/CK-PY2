class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author
        """Создание и подготовка к работе объекта "Book(Книга)"
        :param name: Название
        :param author: Автор
        """

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.name}. Автор: {self.author}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: (name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """Создание и подготовка к работе объекта "PaperBook(Бумажная книга)"
        :param name: Название
        :param author: Автор
        :param pages: Количество страниц
        """
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Страницы должны быть типа int")
        if not pages > 0:
            raise ValueError("Количество страниц не может иметь отрицательное значение")
        self.pages = pages

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: '{self.name}'. Автор: {self.author}. Количество страниц: {self.pages}."


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """Создание и подготовка к работе объекта "AudioBook(Аудиокнига)"
        :param name: Название
        :param author: Автор
        :param duration: Продолжительность аудиозаписи
        """
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if not duration > 0:
            raise ValueError("Продолжительность не может иметь отрицательное значение")
        self.duration = duration

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: '{self.name}'. Автор: {self.author}. Продолжительность: {self.duration}."


print(PaperBook("Подсказчик", "Донато Карризи", 456))
print(AudioBook("Потерянные девушки Рима", "Донато Карризи", 16.24))
