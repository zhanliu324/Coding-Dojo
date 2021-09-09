import pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

pet1 = pet.Pet("Yuki", "Cat", "Catch a ball", "Nyan Nyan")
ninja1 = Ninja("Hanzo", "Hasashi", "Beef", "Fish", pet1)

ninja1.feed()
ninja1.bathe()
ninja1.walk()

print(f"Ninja: {ninja1.first_name} {ninja1.last_name}, Pet: {ninja1.pet.name}\nHeath is {ninja1.pet.health}, Energy is {ninja1.pet.energy}")


class Dog(pet.Pet):
    def __init__(self, name, gender, tricks, noise, health = 100, energy = 100):
        super().__init__(name, 'Dog', tricks, noise, health, energy)
        self.gender = gender
    def play_twice(self):
        super().play()
        print(self.health)
        super().play()
        print(self.health)
        return self


dog1 = Dog("Ric", "Male", "Baseball", "Wa Wa")
dog1.play_twice()