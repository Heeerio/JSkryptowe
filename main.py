from JSkryptowe.logic.statistics_report import save_most_reserved_books_to_txt, save_most_reserved_books_chart
from gui.gui import main

if __name__ == '__main__':
    main()
    save_most_reserved_books_to_txt()        # wygeneruje plik .txt
    save_most_reserved_books_chart()         # wygeneruje wykres PNG
