import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('book_name', ['А','Гиперион','А'*40])
    def test_add_new_book_length_of_book_between_0_and_41_book_added (self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    @pytest.mark.parametrize('book_name', ['А'*41,'А'*45, ''])
    def test_add_new_book_length_of_book_is_41_or_more_or_equals_zero_book_not_added (self, collector, book_name):
        assert book_name not in collector.books_genre

    def test_add_new_book_add_book_twice_second_book_not_added (self, collector):
        collector.add_new_book('Гиперион')
        collector.add_new_book('Гиперион')
        assert list(collector.books_genre.keys()).count('Гиперион') == 1

    def test_add_new_book_added_book_without_genre (self, collector):
        collector.add_new_book('Гиперион')
        assert collector.books_genre.get('Гиперион') == ''
    
    def test_set_book_genre_existent_genre (self, collector):
        collector.add_new_book('Гиперион')
        collector.set_book_genre('Гиперион','Фантастика')
        assert collector.books_genre.get('Гиперион') == 'Фантастика'

    def test_set_book_genre_change_genre_genre_changed (self, collector):
        collector.add_new_book('Гиперион')
        collector.set_book_genre('Гиперион','Фантастика')
        collector.set_book_genre('Гиперион','Комедии')
        assert collector.books_genre.get('Гиперион') == 'Комедии'

    def test_set_book_genre_nonexistent_genre (self, collector):
        collector.add_new_book('Гиперион')
        collector.set_book_genre('Гиперион','Мелодрама')
        assert collector.books_genre.get('Гиперион') == ''

    def test_get_book_genre_existent_book (self, collector):
        collector.add_new_book('Гиперион')
        collector.set_book_genre('Гиперион','Фантастика')
        assert collector.get_book_genre('Гиперион') == 'Фантастика'

    def test_get_book_genre_nonexistent_book (self, collector):
        assert collector.get_book_genre('Книга, которой нет в списке') == None

    def test_get_books_with_specific_genre_existent_genre (self, collector):
        collector.add_new_book('Гиперион')
        collector.set_book_genre('Гиперион','Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно','Ужасы')        
        collector.add_new_book('Темная башня')
        collector.set_book_genre('Темная башня','Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гиперион','Темная башня']

    @pytest.mark.parametrize('genre_name', ['Мелодрама',''])
    def test_get_books_with_specific_genre_nonexistent_genre (self, collector, genre_name):
        collector.add_new_book('Гиперион')
        collector.set_book_genre('Гиперион','Фантастика')
        assert collector.get_books_with_specific_genre(genre_name) == []

    def test_get_books_genre_dict_not_empty (self, collector):
        collector.add_new_book('Гиперион')
        collector.set_book_genre('Гиперион','Фантастика')
        assert collector.books_genre == {'Гиперион': 'Фантастика'}

    def test_get_books_genre_empty_dict (self, collector):
        assert collector.books_genre == {}

    def test_get_books_for_children_input_book_is_for_children_book_added (self, collector):
        collector.add_new_book('Гиперион')
        collector.set_book_genre('Гиперион','Фантастика')
        assert 'Гиперион' in collector.get_books_for_children()

    def test_get_books_for_children_input_book_adult_rating_book_not_added (self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно','Ужасы')
        assert 'Оно' not in collector.get_books_for_children()


    def test_add_book_in_favorites_add_existent_book_book_added (self, collector):
        collector.add_new_book('Гиперион')
        collector.add_book_in_favorites('Гиперион')
        assert 'Гиперион' in collector.favorites

    def test_add_book_in_favorites_add_nonexistent_book_book_not_added (self, collector):
        collector.add_book_in_favorites('Книга, которой нет в списке')
        assert 'Книга, которой нет в списке' not in collector.favorites

    def test_add_book_in_favorites_add_book_twice_second_book_not_added (self, collector):
        collector.add_new_book('Гиперион')
        collector.add_book_in_favorites('Гиперион')
        collector.add_book_in_favorites('Гиперион')
        assert collector.favorites.count('Гиперион') == 1

    def test_delete_book_from_favorites_delete_existent_book_book_deleted (self, collector):
        collector.add_new_book('Гиперион')
        collector.add_book_in_favorites('Гиперион')
        collector.delete_book_from_favorites('Гиперион')
        assert collector.favorites.count('Гиперион') == 0

    def test_delete_book_from_favorites_delete_nonexistent_book (self, collector):
        collector.delete_book_from_favorites('Книга, которой нет в списке')
        assert 'Книга, которой нет в списке' not in collector.favorites

    def test_get_list_of_favorites_books_list_not_empty (self, collector):
        collector.add_new_book('Гиперион')
        collector.add_book_in_favorites('Гиперион')
        assert collector.favorites == ['Гиперион']

    def test_get_list_of_favorites_books_empty_list (self, collector):
        assert collector.favorites == []    
