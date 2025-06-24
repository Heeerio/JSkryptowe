
# Przykładowe dane wejściowe i wyjściowe

## Wyszukiwanie książki

**Dane wejściowe:** `"Wiedźmin"`  
**Wyjściowe:**  
```
Wiedźmin by Andrzej Sapkowski
```

## Rezerwacja książki

**Dane wejściowe:**  
- Imię: `"Anna"`  
- Tytuł: `"Hobbit"`

**Wyjście:**  
```
Zarezerwowano książkę.
```

## Lista rezerwacji

**Wyjście:**  
```
Anna zarezerwował(a) Hobbit
```

## Usuwanie rezerwacji

**Dane wejściowe:**  
- Imię: `"Anna"`  
- Tytuł: `"Hobbit"`

**Wyjście:**  
```
Rezerwacja usunięta.
```

## Dane JSON – `books.json`
```json
[
  {
    "title": "Wiedzmin: Ostatnie zyczenie",
    "author": "Andrzej Sapkowski"
  },
  {
    "title": "Hobbit",
    "author": "J.R.R. Tolkien"
  }
]
```

## Dane JSON – `reservations.json`
```json
[
  {
    "user": "Anna",
    "book_title": "Hobbit"
  }
]
```
