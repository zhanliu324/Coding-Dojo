class Animal:
    def __init__(self, name, age, health=100, happiness=100) -> None:
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Animal name: {self.name}, health: {self.health}, happiness: {self.happiness}.")
        return self
    
    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

class Lion(Animal):
    def __init__(self, name, age, gender,health=120, happiness=90) -> None:
        super().__init__(name, age, health=health, happiness=happiness)
        self.gender = gender

    def feed(self):
        self.health += 8
        self.happiness += 15
        return self

class Tiger(Animal):
    def __init__(self, name, age, health=95, happiness=110) -> None:
        super().__init__(name, age, health=health, happiness=happiness)

    def feed(self):
        self.health += 15
        self.happiness += 9
        return self

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name, age, gender):
        self.animals.append( Lion(name, age, gender) )
    def add_tiger(self, name, age):
        self.animals.append( Tiger(name, age) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 10, 'M')
zoo1.add_lion("Simba", 15, "F")
zoo1.add_tiger("Rajah", 5)
zoo1.add_tiger("Shere Khan", 8)
zoo1.print_all_info()
