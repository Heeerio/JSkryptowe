import unittest
from unittest.mock import patch, mock_open
from logic import logic


class TestLibraryLogic(unittest.TestCase):

    @patch('logic.logic.load_data')
    def test_search_books_found(self, mock_load_data):
        mock_load_data.return_value = [
            {'title': 'Wiedźmin', 'author': 'Andrzej Sapkowski'},
            {'title': 'Lalka', 'author': 'Bolesław Prus'}
        ]
        result = logic.search_books("Wiedź")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['title'], 'Wiedźmin')

    @patch('logic.logic.load_data')
    def test_search_books_not_found(self, mock_load_data):
        mock_load_data.return_value = [
            {'title': 'Lalka', 'author': 'Bolesław Prus'}
        ]
        result = logic.search_books("Python")
        self.assertEqual(result, [])

    @patch('logic.logic.load_data')
    @patch('logic.logic.save_data')
    def test_reserve_book_success(self, mock_save_data, mock_load_data):
        mock_load_data.return_value = []
        logic.reserve_book("Anna", "Lalka")
        mock_save_data.assert_called_once()
        saved = mock_save_data.call_args[0][1]
        self.assertEqual(saved[0]['user'], 'Anna')
        self.assertEqual(saved[0]['book_title'], 'Lalka')

    @patch('logic.logic.load_data')
    def test_reserve_book_already_reserved(self, mock_load_data):
        mock_load_data.return_value = [{'user': 'Kasia', 'book_title': 'Lalka'}]
        with self.assertRaises(Exception) as context:
            logic.reserve_book("Anna", "Lalka")
        self.assertIn("już zarezerwowana", str(context.exception))

    @patch('logic.logic.load_data')
    def test_list_reservations(self, mock_load_data):
        mock_load_data.return_value = [{'user': 'Jan', 'book_title': 'Wiedźmin'}]
        result = logic.list_reservations()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['user'], 'Jan')

    @patch('logic.logic.load_data')
    @patch('logic.logic.save_data')
    def test_delete_reservation_success(self, mock_save_data, mock_load_data):
        mock_load_data.return_value = [
            {'user': 'Anna', 'book_title': 'Lalka'},
            {'user': 'Jan', 'book_title': 'Wiedźmin'}
        ]
        logic.delete_reservation("Anna", "Lalka")
        updated_data = mock_save_data.call_args[0][1]
        self.assertEqual(len(updated_data), 1)
        self.assertEqual(updated_data[0]['book_title'], 'Wiedźmin')

    @patch('logic.logic.load_data')
    def test_delete_reservation_not_found(self, mock_load_data):
        mock_load_data.return_value = [{'user': 'Jan', 'book_title': 'Wiedźmin'}]
        with self.assertRaises(Exception) as context:
            logic.delete_reservation("Anna", "Lalka")
        self.assertIn("Nie znaleziono", str(context.exception))


class TestHelperFunctions(unittest.TestCase):
    def test_search_books_inline(self):
        books = [
            {'title': 'Wiedźmin', 'author': 'Andrzej Sapkowski'},
            {'title': 'Lalka', 'author': 'Bolesław Prus'}
        ]
        result = logic.search_books_inline(books, 'sap')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['author'], 'Andrzej Sapkowski')

    def test_get_reserved_books_by_user(self):
        reservations = [
            {'username': 'Anna', 'book_title': 'Lalka'},
            {'username': 'Anna', 'book_title': 'Wiedźmin'},
            {'username': 'Jan', 'book_title': 'Quo Vadis'}
        ]
        result = logic.get_reserved_books_by_user(reservations, 'Anna')
        self.assertEqual(len(result), 2)
        self.assertIn('Lalka', result)
        self.assertIn('Wiedźmin', result)


if __name__ == '__main__':
    unittest.main()
