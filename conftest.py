import pytest

@pytest.fixture # фикстура, которая создаёт объект класса BooksCollector
def collector():
    collector = BooksCollector()
    return collector