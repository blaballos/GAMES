def show_role():
    role = input('1. Warrior\n2. Wizard\n3. Golem\nSelect a role for view its features: ')
    
    if role == '1':
        print('\nCharacteristics of the Warrior:')
        print('Health: 150 ❤\nDamage: 120 🗡\nAttack speed: 1.2s 🕰')
    elif role == '2':
        print('\nCharacteristics of the Wizard:')
        print('Health: 120 ❤\nDamage: 170 🗡\nAttack speed: 1.6s 🕰')
    elif role == '3':
        print('\nCharacteristics of the Golem:')
        print('Health: 350 ❤\nDamage: 200 🗡\nAttack speed: 2.1s 🕰')
        
    confirm = input('\n1. Back\nConfirm\nSelect an option: ')
    return confirm