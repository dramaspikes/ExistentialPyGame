class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

def attack(target):
    target.health -=5
    if target.health > 0:
        print(f"\nYou took 5HP from {target.name}. It now has {target.health}HP.")
    else:
        print(f"\n{target.name} has been slain.")
        enemies.remove(target)

dread = Enemy("Existential Dread", 20)
memories = Enemy("Memories of the Past", 35)
enemies = [dread, memories]
print("\nYou find yourself up against two formidable opponents.")

for enemy in enemies:
    print(f"\n{enemy.name} has {enemy.health}HP.")

print("\nGood luck!")

first = True

while dread.health > 0 or memories.health > 0:
    if first == True:
        decision = input("\nWill you attack? (Type 'Yes' or 'No'): ").lower()
    else:
        decision = input("\nWill you attack again? (Type 'Yes' or 'No'): ").lower()

    if decision == "yes":
        if dread.health > 0 and memories.health > 0:
            target = input("\nWhich enemy will you attack? (Type 'Dread' or 'Memories'): ").lower()
            if target == "dread":
                attack(dread)
                first = False
            elif target == "memories":
                attack(memories)
                first = False
            else:
                print("\nSorry, that's not a current opponent.")
        else:
            if dread.health > 0:
                attack(dread)
            else:
                attack(memories)

    elif decision == "no":
        if len(enemies) > 1:
            if first == True:
                print(f"\n{enemies[0].name} and {enemies[1].name} remain untouched.")
            else:
                print(f"\n{enemies[0].name} and {enemies[1].name} loom.")
        else:
            print(f"\n{enemies[0].name} looms.")
    else:
        print(f"\nNot sure why you said '{decision}', but next time please enter 'Yes' or 'No'")

print(f"\nYou conquered Existential Dread and Memories of the Past. Congratulations!")