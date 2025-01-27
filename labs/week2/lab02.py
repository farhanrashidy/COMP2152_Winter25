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


