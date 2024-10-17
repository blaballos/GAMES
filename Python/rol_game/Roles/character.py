from Actions.attack import Attack
from Actions.defend import Defend

class Character(Attack, Defend):
    def __init__(self, name, health, damage, attack_speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.attack_speed = attack_speed