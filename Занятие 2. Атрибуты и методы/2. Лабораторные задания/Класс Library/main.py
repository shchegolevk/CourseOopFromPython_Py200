# База данных книг для проверки
from typing import List

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

# TODO Импортируйте и скопируйте ранее написанный класс Book
class Book:
    def __init__(self, id_, name, pages):
        # pass # TODO дописать метод
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        # pass # TODO дописать метод
        return f'Книга "{self.name}"'
    def __repr__(self):
        #pass # TODO дописать метод
        return f"{self.__class__.__name__}(id_={str(self.id)}, name='{self.name}', pages={str(self.pages)})"

class Library:

    def __init__(self, books):
        """
        Не забудьте про 'Конструктор должен принимать необязательный аргумент со значением по умолчанию. Если пользователь
        его не передал, то библиотека инициализируется с пустым списком книг.'
        :param books:
        """
        # pass # TODO дописать метод
        if books is None:
            self.books = []
        elif isinstance(books, List):
           self.books = books
        else:
            raise TypeError("При создании библиотеки должен быть передан список книг или None")

    def get_next_book_id(self):
        """
        Необходимо узнать последнюю книгу в библиотеке, посмотреть атрибут 'id' этой книги и вернуть следующее
        значение после этого `id`
        :return:
        """
        pass # TODO дописать метод

        return max(self.books, key=lambda x: x['id']) + 1 # max(data, key=lambda x: x['price'])

    def get_index_by_book_id(self, id_):
        """
        Так как в библиотеке книги хранятся в списке, то данная функция возвращает индекс, где книга с определенным
        `id` хранится в списке книг. Для примера. [Book(id=1, ...), Book(id=2, ...)] книга с id=2 хранится
        на индексе 1 списка книг
        :param id_: id книги
        :return: индекс, где лежит книга в списке книг
        """
        pass # TODO дописать метод
        self.books.index()

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
