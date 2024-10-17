import random

class Defend():
    def defend(self):
        random_number = random.randint(0,7)
        
        if random_number == 6:
            print(f'{self.name} successfully defended himself')
        else:
            print(f'{self.name} could not avoid the hit')