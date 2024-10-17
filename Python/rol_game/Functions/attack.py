def attack(character, enemy):
    random_number = character.attack()
    
    if random_number == 0:
        enemy.health = enemy.health 
    elif random_number == 6:
        if character.role == 'warrior':
            enemy.health -= 145
        elif character.role == 'wizard':
            enemy.health -= 195
        elif character.role == 'golem':
            enemy.health -= 225
        elif character.role == 'enemy':
            enemy.health -= 275
    else:
        if character.role == 'warrior':
            enemy.health -= 120
        elif character.role == 'wizard':
            enemy.health -= 170
        elif character.role == 'golem':
            enemy.health -= 200
        elif character.role == 'enemy':
            enemy.health -= 250
        
    print(f'{enemy.name} has {enemy.health} health points remaining')