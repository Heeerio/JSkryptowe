from .statistics import get_most_reserved_books

import matplotlib.pyplot as plt

def save_most_reserved_books_to_txt(filename='most_reserved_books.txt'):
    stats = get_most_reserved_books()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Najczęściej rezerwowane książki:\n\n")
        for title, count in stats:
            f.write(f"{title} – {count} rezerwacji\n")

def save_most_reserved_books_chart(filename='most_reserved_books.png'):
    stats = get_most_reserved_books()
    if not stats:
        print("Brak danych do wykresu.")
        return

    titles, counts = zip(*stats)

    plt.figure(figsize=(10, 6))
    plt.bar(titles, counts, color='skyblue')
    plt.xlabel('Tytuł książki')
    plt.ylabel('Liczba rezerwacji')
    plt.title('Najczęściej rezerwowane książki')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    if __name__ == "__main__":
        save_most_reserved_books_chart()
        print("Wykres został zapisany.")

