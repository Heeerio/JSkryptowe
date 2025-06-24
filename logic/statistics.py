
from collections import Counter
from data.data import load_data, RESERVATIONS_FILE, BOOKS_FILE


def get_most_reserved_books():
    books = load_data(BOOKS_FILE)
    reservations = load_data(RESERVATIONS_FILE)
    book_titles_reserved = [r['book_title'] for r in reservations]
    counter = Counter(book_titles_reserved)

    # Uzupełniamy wszystkie książki, nawet jeśli nie mają rezerwacji
    all_books_with_counts = []
    for book in books:
        title = book['title']
        count = counter.get(title, 0)
        all_books_with_counts.append((title, count))

    # Sortujemy malejąco po liczbie rezerwacji
    all_books_with_counts.sort(key=lambda x: x[1], reverse=True)
    return all_books_with_counts


