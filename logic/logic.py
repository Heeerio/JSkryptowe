# logic.py

from data.data import load_data, save_data, BOOKS_FILE, RESERVATIONS_FILE

def search_books(keyword):
    books = load_data(BOOKS_FILE)
    keyword = keyword.lower()
    return [book for book in books if keyword in book['title'].lower() or keyword in book['author'].lower()]

def reserve_book(user, book_title):
    reservations = load_data(RESERVATIONS_FILE)
    for res in reservations:
        if res['book_title'].lower() == book_title.lower():
            raise Exception("Ta książka jest już zarezerwowana.")
    reservations.append({"user": user, "book_title": book_title})
    save_data(RESERVATIONS_FILE, reservations)

def list_reservations():
    return load_data(RESERVATIONS_FILE)

def delete_reservation(user, book_title):
    reservations = load_data(RESERVATIONS_FILE)
    updated = [res for res in reservations if not (res['user'] == user and res['book_title'].lower() == book_title.lower())]
    if len(updated) == len(reservations):
        raise Exception("Nie znaleziono takiej rezerwacji.")
    save_data(RESERVATIONS_FILE, updated)

def search_books_inline(books, query):  # zmieniona nazwa
    query = query.lower()
    filtered_books = list(filter(lambda book: query in book['title'].lower() or query in book['author'].lower(), books))
    return filtered_books

def get_reserved_books_by_user(reservations, username):
    return list(map(lambda res: res['book_title'], filter(lambda res: res['username'] == username, reservations)))
