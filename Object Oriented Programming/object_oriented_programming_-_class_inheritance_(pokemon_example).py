class Creature: # this is the PARENT CLASS
    def __init__(self, name):
        self.name = name

    def battle(self):
        print(f"{self.name} enters the gym and starts a battle.")

    def describe(self):
        pass


class Trainer(Creature): # this is a CHILD CLASS
    def __init__(self, name, how_many_caught):
        super().__init__(name)
        self.how_many_caught = how_many_caught

    def catch(self):
        print(f"{self.name} is catching them all! But he's only caught {self.how_many_caught} so far.")

    def describe(self):
        print(f"{self.name} is a trainer. He's wearing a hat.")


class Pokemon(Creature): # this is a CHILD CLASS
    def __init__(self, name, pokemon_type, first_evolution):
        super().__init__(name)
        self.pokemon_type = pokemon_type
        self.first_evolution = first_evolution

    def evolve(self):
        print(f"{self.name} is a {self.pokemon_type} type pokemon and just evolved into a {self.first_evolution}!")

    def describe(self):
        print(f"{pikachu.name} is a {pikachu.pokemon_type} pokemon and it can evolve into {pikachu.first_evolution}.")


ian = Trainer("Ian", 5)
pikachu = Pokemon("Pikachu", "electric", "Raichu")


pikachu.describe()
input()
pikachu.battle()
input()
pikachu.evolve()
input()
ian.evolve()
input()
ian.catch()
input()
ian.battle()

