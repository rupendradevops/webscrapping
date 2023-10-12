# Parent class
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

# Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, breed):
        super().__init__("Cat")
        self.breed = breed

    def make_sound(self):
        return "Meow!"

# Creating instances of child classes
dog = Dog("Golden Retriever")
cat = Cat("Siamese")

# Using methods from the parent and child classes
print(dog.species)  # Output: Dog
print(dog.breed)    # Output: Golden Retriever
print(dog.make_sound())  # Output: Woof!

print(cat.species)  # Output: Cat
print(cat.breed)    # Output: Siamese
print(cat.make_sound())  # Output: Meow!
