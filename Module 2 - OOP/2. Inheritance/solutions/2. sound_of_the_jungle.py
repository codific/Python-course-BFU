from os import linesep

class Animal:

    def __init__(self, name, age, gender, color):
        self.name = name
        self.age = age
        self.gender = gender
        self.color = color

    def __str__(self):
        result = f'My name is {self.name}{linesep}' \
            f'I am {self.age} years old{linesep}' \
            f'I am {self.gender}{linesep}' \
            f'and I am {self.color}'
        return result

class Snake(Animal):

    def make_sound(self):
        print('I am a snake and I rattle.')

class Tiger(Animal):

    def make_sound(self):
        print('I am a tiger and I roar.')


class Bird(Animal):

    def make_sound(self):
        print('I am a bird and I tweet.')


class Frog(Animal):

    def make_sound(self):
        print('I am a frog and I quack.')


animals = [
    Snake('Kim', 6, 'female', 'black'),
    Tiger('Simba', 4, 'male', 'orange'),
    Bird('Max', 5, 'male', 'blue'),
    Frog('Sarah', 3, 'female', 'green')
]

for animal in animals:
    print(animal)
    animal.make_sound()
    print('=' * 30)