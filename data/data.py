import json

BOOKS_FILE = 'storage/books.json'
RESERVATIONS_FILE = 'storage/reservations.json'

def load_data(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
