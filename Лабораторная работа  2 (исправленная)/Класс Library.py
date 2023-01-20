# К сожалению, не знаю как импортировать BOOKS_DATABASE и Book, поэтому они были скопированы из предыдущего файла
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """Создание и подготовка к работе объекта "Книга"
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})"


class Library:
    def __init__(self, books: list[Book] = None):
        """Создание и подготовка к работе объекта "Библиотека"
        :param books: Список книг
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """Метод, возвращающий идентификатор для добавления новой книги в библиотеку"
        :return: Если книг в библиотеке нет, то возвращаем 1, если книга есть, то вернуть идентификатор последней
        книги, увеличенный на 1
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id_: int) -> int:
        """Функция(метод), которая(который) возвращает индекс книги в списке
        :return: index
        :raise ValueError: Если книги нет, то вызваем ошибку с сообщением: "Книги с запрашиваемым id не существует"
        """
        for index, book in enumerate(self.books):
            if book.id == id_:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
