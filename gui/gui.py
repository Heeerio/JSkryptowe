
import tkinter as tk
from tkinter import messagebox
from api.api import perform_search_gui, perform_reservation_gui, show_reservations_gui, show_books_gui, delete_reservation_gui

def main():
    root = tk.Tk()
    root.title("System Biblioteczny")
    root.geometry("400x350")

    tk.Button(root, text="Szukaj książki", command=perform_search_gui, width=30).pack(pady=5)
    tk.Button(root, text="Zarezerwuj książkę", command=perform_reservation_gui, width=30).pack(pady=5)
    tk.Button(root, text="Pokaż wszystkie książki", command=show_books_gui, width=30).pack(pady=5)
    tk.Button(root, text="Pokaż rezerwacje", command=show_reservations_gui, width=30).pack(pady=5)
    tk.Button(root, text="Usuń rezerwację", command=delete_reservation_gui, width=30).pack(pady=5)
    tk.Button(root, text="Wyjście", command=root.quit, width=30).pack(pady=5)

    root.mainloop()
