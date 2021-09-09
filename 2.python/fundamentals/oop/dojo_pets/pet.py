class Pet:
    def __init__(self, name, type, tricks, noise, health = 100, energy = 100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.pet_noise = noise
        self.health = health
        self.energy = energy
    
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(self.pet_noise)
        return self