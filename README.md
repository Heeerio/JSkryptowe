# System Rezerwacji Książek – Aplikacja z GUI

## Opis projektu

Projekt ten to prosty system rezerwacji książek napisany w języku **Python**, z wykorzystaniem biblioteki **tkinter** do stworzenia graficznego interfejsu użytkownika. Aplikacja umożliwia użytkownikom przeglądanie dostępnych książek, dokonywanie rezerwacji oraz zapis danych do pliku.

---

##  Funkcjonalności

- Przeglądanie listy książek z GUI
- Rezerwacja wybranej pozycji przez użytkownika
- Zapisywanie rezerwacji do pliku `reservations.json`
- Automatyczne wczytywanie książek z pliku `books.json`
- Obsługa wyjątków (np. brak danych)
- Walidacja danych wejściowych

---

##  Struktura projektu
library_reservation_system/
│
├── main.py # Główny plik uruchamiający aplikację
├── api/
│ └── api.py # Komunikacja GUI z logiką aplikacji
├── data/
│ └── data.py # Ewentualna inicjalizacja danych
├── logic/
│ └── logic.py # Logika biznesowa aplikacji
├── models/
│ └── models.py # Klasy danych (Book, Reservation)
├── gui/
│ └── gui.py # Interfejs użytkownika (tkinter)
├── storage/
│ ├── books.json # Plik z danymi książek
│ └── reservations.json # Plik z zapisanymi rezerwacjami
└── README.md # Ten plik


---

## 🛠️ Technologie

- Python 3.x
- tkinter
- json
- datetime
- os

---

## 🚀 Uruchomienie aplikacji

1. Upewnij się, że masz zainstalowanego Pythona 3.x.
2. Upewnij się, że w folderze `storage/` znajdują się pliki `books.json` i `reservations.json`.
3. W terminalu przejdź do katalogu projektu.
4. Uruchom aplikację:

```bash
python main.py
