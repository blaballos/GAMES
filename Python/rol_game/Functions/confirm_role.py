# IMPORTS

def confirm_role(name, role, confirmation):
    if confirmation == '2':
        if role == '1':
            character = 'Warrior'
        elif role == '2':
            character = 'Wizard'
        elif role == '3':
            character = 'Golem'
            
        enemy = 'Enemy'
        
    return character, enemy