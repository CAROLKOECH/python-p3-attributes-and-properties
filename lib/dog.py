APPROVED_BREEDS = [
    "Mastiff", "Chihuahua", "Corgi", "Shar Pei",
    "Beagle", "French Bulldog", "Pug", "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")
