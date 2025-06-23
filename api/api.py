
from logic.logic import search_books, reserve_book, list_reservations, delete_reservation
from data.data import load_data, BOOKS_FILE
from tkinter import simpledialog, messagebox

def perform_search_gui():
    keyword = simpledialog.askstring("Szukaj książki", "Podaj tytuł lub autora:")
    if keyword:
        results = search_books(keyword)
        if results:
            books_text = "\n".join(f"{book['title']} by {book['author']}" for book in results)
            messagebox.showinfo("Znalezione książki", books_text)
        else:
            messagebox.showinfo("Brak wyników", "Nie znaleziono książek.")

def perform_reservation_gui():
    user = simpledialog.askstring("Rezerwacja", "Podaj swoje imię:")
    book_title = simpledialog.askstring("Rezerwacja", "Podaj tytuł książki:")
    if user and book_title:
        try:
            reserve_book(user, book_title)
            messagebox.showinfo("Sukces", "Zarezerwowano książkę.")
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

def show_reservations_gui():
    reservations = list_reservations()
    if reservations:
        res_text = "\n".join(f"{r['user']} zarezerwował(a) {r['book_title']}" for r in reservations)
        messagebox.showinfo("Rezerwacje", res_text)
    else:
        messagebox.showinfo("Rezerwacje", "Brak rezerwacji.")

def show_books_gui():
    books = load_data(BOOKS_FILE)
    if books:
        books_text = "\n".join(f"{b['title']} by {b['author']}" for b in books)
        messagebox.showinfo("Wszystkie książki", books_text)
    else:
        messagebox.showinfo("Biblioteka", "Brak książek w bibliotece.")

def delete_reservation_gui():
    user = simpledialog.askstring("Usuń rezerwację", "Podaj swoje imię:")
    book_title = simpledialog.askstring("Usuń rezerwację", "Podaj tytuł książki do usunięcia:")
    if user and book_title:
        try:
            delete_reservation(user, book_title)
            messagebox.showinfo("Sukces", "Rezerwacja usunięta.")
        except Exception as e:
            messagebox.showerror("Błąd", str(e))
