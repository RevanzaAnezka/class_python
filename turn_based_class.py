import random 

class Character:
  def __init__(self, name, health):
    self.name = name
    self.health = health

  def attack(self, monster):
    pass

  def special(self, monster):
    pass

  # BONUS 4: heal
  def heal(self):
    amount = random.randint(15, 25)
    self.health += amount
    print(f"{self.name} heals {amount} HP!")

  def take_damage(self, damage):
    self.health = max(0, self.health-damage)

  def display_status(self):
    print(f"{self.name} | HP: {self.health}")

class Warrior(Character):
  def __init__(self, name, health):
    super().__init__(name, health)

  def attack(self, monster):
    damage = random.randint(8, 15)
    print(f"{self.name} slashes forward for {damage} damage!")
    monster.take_damage(damage)

  def special(self, monster):
    damage = random.randint(22, 30)
    print(f"{self.name} sends out wolves to attack for {damage} damage!")
    monster.take_damage(damage)

class Mage(Character):
  def __init__(self, name, health):
    super().__init__(name, health)
  
  def attack(self, monster):
    damage = random.randint(8, 14)
    print(f"{self.name} casts a spell for {damage} damage!")
    monster.take_damage(damage)

  def special(self, monster):
    damage = random.randint(25, 32)
    print(f"{self.name} casts a poison spell for {damage} damage!")
    monster.take_damage(damage)

class Archer(Character):
  def __init__(self, name, health):
    super().__init__(name, health)
  
  def attack(self, monster):
    damage = random.randint(10, 16)
    print(f"{self.name} shoots an arrow for {damage} damage!")
    monster.take_damage(damage)

  def special(self, monster):
    damage = random.randint(6, 10) * 3
    print(f"{self.name} shoots a flaming arrow for {damage} damage!")
    monster.take_damage(damage)

class Monster:
  def __init__(self, name, health, damage=10):
    self.name = name
    self.health = health
    self.damage = damage

  def attack(self, character):
    damage = random.randint(self.damage - 3, self.damage + 3)
    print(f"{self.name} hits {character.name} for {damage} damage!")
    character.take_damage(damage)
  
  def take_damage(self, damage):
    self.health = max(0, self.health-damage)

  def display_status(self):
    print(f"{self.name} | HP: {self.health}")

def start_battle(character, monster):
  character.display_status()
  monster.display_status()

  while character.health > 0 and monster.health > 0:
    if character.health < 30:
      character.heal()
    elif random.random() < 0.3:
      character.special(monster)
    else:
      character.attack(monster)

    if monster.health > 0:
      monster.attack(character)

    character.display_status()
    monster.display_status()

  if character.health > 0:
    print(f"{character.name} won the game!")
  else:
    print(f"{monster.name} won the game!")

warrior = Warrior("Revvan", 100)
archer = Archer("Anezka", 100)
mage = Mage("Lauven", 100)

start_battle(warrior, Monster("Ogre", 100, 9))
start_battle(archer, Monster("Wyvern", 120, 9))
start_battle(mage, Monster("Minion", 60, 6))

print("Choose your champion!")
print("(1) Warrior")
print("(2) Archer")
print("(3) Mage")
choice = input("1/2/3: ")

if choice == "1":
    player = Warrior("Revvan", 100)
elif choice == "2":
    player = Archer("Anezka", 100)
else:
    player = Mage("Lauven", 100)

start_battle(player, Monster("Dragon", 85))