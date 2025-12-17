class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species


class Mammal(Animal):

    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color


class Bird(Animal):

    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.wing_span = wing_span

class Reptile(Animal):

    def __init__(self, name, species, scale_type):
        super().__init__(name, species)
        self.scale_type = scale_type


class Zoo:

    def __init__(self, animals=[]):
        self.animals = animals

    def add_animals(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)

    def remove_animal(self, name):
        self.animals = list(filter(lambda animal: animal.name != name, self.animals))

    def list_animals(self):
        for animal in self.animals:
            print(animal.name, animal.species)

    def get_animals_by_species(self, species):
        result = list(filter(lambda animal: animal.species == species, self.animals))
        for an in result:
            print(an.name, an.species)
    def count_animals(self):
        print('Total animals:', len(self.animals))

jack = Mammal('Jack', 'Lion', 'Orange')
simba = Mammal('Simba', 'Lion', 'Orange')
bob = Bird('Bob', 'Eagle', '1.5')
morty = Reptile('Morty', 'Python', 'Diamond')

zoo = Zoo()

zoo.add_animals(jack)
zoo.add_animals(simba)
zoo.add_animals(bob)
zoo.add_animals(morty)
# print('Before remove:', zoo.animals)
# zoo.remove_animal('Simba')
# print('After remove: ', zoo.animals)

zoo.list_animals()
zoo.get_animals_by_species('Lion')

zoo.count_animals()