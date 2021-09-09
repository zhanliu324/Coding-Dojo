from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

round = 1
while michelangelo.health > 0 and jack_sparrow.health > 0:
    print(f"Round {round}")
    michelangelo.attack(jack_sparrow)
    jack_sparrow.attack(michelangelo)
    michelangelo.show_stats()
    jack_sparrow.show_stats()
    round += 1

print(f"Total number of rounds: {round}.")
if michelangelo.health > jack_sparrow.health:
    print(f"{michelangelo.name} wins!")
else:
    print(f"{jack_sparrow.name} wins!")