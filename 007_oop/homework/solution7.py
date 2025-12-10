

class Animal:
    def  __init__(self, name: str, species: str):
            self.name = name
            self.species = species

    def animal_data(self):
        return f'{self.name} {self.species}\n'


class Mammal(Animal):
    def __init__(self, name: str, species: str, fur_color: str):
        super().__init__(name, species)
        self.fur_color = fur_color


class Bird(Animal):
    def __init__(self, name: str, species: str, wing_span: float):
        super().__init__(name, species)
        self.wing_span = wing_span


class Reptile(Animal):
    def __init__(self, name: str, species: str, scale_type: str):
        super().__init__(name, species)
        self.scale_type = scale_type


class Zoo:
    animal_counter = 0
    def __init__(self, animals=None):
        if animals is None:
            self.animals = []
        else:
            self.animals = animals

    # Method to add animals
    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
            self.animal_counter += 1
    # Method to list animals
    def list_animals(self):
        for animal in self.animals:
            print(animal.animal_data())
    # Method to to get animals by species
    def get_animals_by_species(self, species):
        for animal in self.animals:
            if species == animal.species:
                print(animal.animal_data())
    # Method to remove animals
    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            self.animal_counter -= 1
    # Method to count animals
    def count_animals(self):
        return self.animal_counter
        

my_zoo = Zoo()
monkey_Lusy = Mammal("Lucy", "Mammal", "brown")
elephant_Bo = Mammal("Bo", "Mammal", "brown")
bird_Iggy = Bird("Iggy", "Bird", 96)
turtle_Speedy = Reptile("Speedy", "Reptile", "round")

my_zoo.add_animal(monkey_Lusy)
my_zoo.add_animal(elephant_Bo)
my_zoo.add_animal(bird_Iggy)
my_zoo.add_animal(turtle_Speedy)

print(monkey_Lusy.__dict__)
print(my_zoo.__dict__)

my_zoo.list_animals()
my_zoo.get_animals_by_species("Mammal")
my_zoo.get_animals_by_species("Bird")
my_zoo.get_animals_by_species("Reptile")
print(my_zoo.count_animals())
my_zoo.remove_animal(elephant_Bo)
my_zoo.list_animals()
print(my_zoo.count_animals())


