# TODO скопириуйте и запустите здесь необходимый код
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal: Animal):
    print(animal.speak())
if __name__ == "__main__":
    pass
    dog = Dog()
    cat = Cat()

    make_animal_speak(dog)  # Woof!
    make_animal_speak(cat)  # Meow!