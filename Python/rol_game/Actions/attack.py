import random

class Attack():
    def attack(self):
        random_number = random.randint(0,7)
        
        if random_number == 0:
            print(f'{self.name} his attack failed')
        elif random_number == 6:
            print(f'{self.name} performed a CRTICAL HIT of {self.damage + 25} damage')
        else:
            print(f'{self.name} performed a hit of {self.damage} damage')