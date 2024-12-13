import json

class Person:
    def __init__(self, name="", surname="", address="", postal_code="", pesel=""):
        self.name = name
        self.surname = surname
        self.address = address
        self.postal_code = postal_code
        self.pesel = pesel

    def to_json(self, filepath):
        """Zapisuje obiekt do pliku JSON."""
        with open(filepath, 'w') as f:
            json.dump(self.__dict__, f, ensure_ascii=False, indent=4)

    @staticmethod
    def from_json(filepath):
        """Wczytuje dane z pliku JSON i tworzy obiekt klasy."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        return Person(**data)

# Tworzenie obiektu
osoba = Person(name="Kamil", surname="Kowalski", address="ul. Polna 12, Warszawa", postal_code="00-123", pesel="12345678901")

# Zapis do pliku JSON
plik_json = "dane.json"
osoba.to_json(plik_json)

# Odczyt z pliku JSON
nowa_osoba = Person.from_json(plik_json)
print(nowa_osoba.__dict__)
