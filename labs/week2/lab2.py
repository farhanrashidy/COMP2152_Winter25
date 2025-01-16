import random

try:

    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
    weaponRoll = random.randint(1, 6)
    weaponEquipped = weapons[weaponRoll - 1]
    print(f"Weapon Equipped: {weaponEquipped}")

    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend")
    elif weaponRoll <= 4:
        print("Your weapon is meh")
    else:
        print("Nice weapon, friend")
    if weaponRoll > 1:
        print("Thank goodness you didnt doll the Fist")

    '''
    # Testing for error handling
    chooseWeapon = int(input("Choose your weapon: "))
    print(weapons[chooseWeapon - 1])
    '''


except IndexError:
    print("*** Error: Invalid element index ***")
except Exception:
    print("*** Enter a Number from 1-6 ***")

'''
***** Lab work *****

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "carbon"]
print("Elements: ", elements)
#  git add . && git commit -m "add elements array" && git push

# def funct_name():
#     return True
# def say_greeting(name, message="hi"):
#     print(f" {message}, {name}")
# say_greeting("Maziar")
# say_greeting("Maziar", "Hello")

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer!")
            continue
try:
    elements_selected = get_valid_int_input("Enter the index of the element you like: ")
    # Roll dice
    elementRoll = random.randint(1, 6)
    totalNum = elements_selected + elementRoll

    # Print the result based on the totalNum
    if elementRoll <= 2:
        print("You rolled a weak element, friend.")
    elif elementRoll <= 4:
        print("Yor element is moderate.")
    else:
        print("Nice element.")
except IndexError:
    print("Error: Invalid element index!")        
except Exception as e:
    print(f"An unexpected error occurred: {e}")    
'''
