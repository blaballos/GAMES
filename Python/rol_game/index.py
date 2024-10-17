from Functions.name_character import name_character
from Functions.show_role import show_role
from Functions.confirm_role import confirm_role
from Functions.attack import attack

def main():
    start = input('¡Welcome!\n1. Play\n2. Exit\nSelect an option: ')
    
    if start == '1':
        print('¡Perfect! crete your character')
        name = name_character()
        
        role, confirmation = show_role()
        while confirmation == '1':
            role, confirmation = show_role()
        character, enemy = confirm_role(name, role, confirmation)
        
        # testing
        attack(character, enemy)
        attack(enemy, character)
        
    elif start == '2':
        print('¡See you later!')
        
main()