# Тесты для класса BooksCollector

## Класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector

### Проверка добавления новой книги:

@pytest.mark.parametrize('book_name', ['Гордость и предубеждение и зомби', 'Таня Гроттер', 'Фантастические твари'])
def test_add_new_book(self, book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    assert collector.get_books_genre() == book_name

### Проверка добавления книги с длинным названием:

def test_add_new_book_too_long_name(self):
    collector = BooksCollector()
    collector.add_new_book('Клуб любителей книг и пирогов из картофельных очистков')
    assert 'Клуб любителей книг и пирогов из картофельных очистков' not in collector.get_books_genre()

### Получение жанра книги по названию:

@pytest.mark.parametrize(
    'book_name,genre',
    [
        ['Гордость и предубеждение и зомби', 'Фантастика'],
        ['Таня Гроттер', 'Фантастика'],
        ['Приключения кота Леопольда', 'Комедии'],
        ['Байки из склепа', 'Ужасы']
    ]
)
def test_get_book_genre(self, book_name, genre):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == genre

### Проверка отсутствия жанра у добавленной книги:

def test_new_book_has_no_genre(self):
    collector = BooksCollector()
    collector.add_new_book('Таня Гроттер')
    assert collector.get_book_genre('Таня Гроттер') == ''

### Вывод списка книг с определенным жанром:

@pytest.mark.parametrize(
    'book_name,genre',
    [
        ['Гордость и предубеждение и зомби', 'Фантастика'],
        ['Таня Гроттер', 'Фантастика']
    ]
)
def test_get_books_with_specific_genre(self, book_name, genre):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_books_with_specific_genre(genre) == [book_name]

### Получение словаря books-genre:

def test_get_books_genre(self):
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
    assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Фантастика'}

### Добавление книги в избранное:

@pytest.mark.parametrize('book_name', ['Унесенные ветром'])
def test_add_book_in_favorites(self, book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    assert collector.get_list_of_favorites_books() == [book_name]

### Удаление книги из избранного:

@pytest.mark.parametrize('book_name', ['Убить пересмешника'])
def test_delete_book_from_favorites(self, book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    collector.delete_book_from_favorites(book_name)
    assert collector.get_list_of_favorites_books() == []

### Получение списка избранных книг:

@pytest.mark.parametrize('book_name', ['Унесенные ветром', 'Что делать, если ваш кот хочет вас убить'])
def test_get_list_of_favorites_books(self, book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    assert collector.get_list_of_favorites_books() == [book_name]

### Получение книг, подходящих для детей:
def test_get_books_for_children_book_in_list(self):
    collector = BooksCollector()
    collector.add_new_book('Приключения кота Леопольда')
    collector.set_book_genre('Приключения кота Леопольда', 'Комедии')
    assert collector.get_books_for_children() == ['Приключения кота Леопольда']

### Проверка, что книга с возврастным жанром отсутсвует в списке книг для детей:
def test_get_books_for_children_book_not_in_list(self):
    collector = BooksCollector()
    collector.add_new_book('Байки из склепа')
    collector.set_book_genre('Байки из склепа', 'Ужасы')
    assert 'Байки из склепа' not in collector.get_books_for_children()

