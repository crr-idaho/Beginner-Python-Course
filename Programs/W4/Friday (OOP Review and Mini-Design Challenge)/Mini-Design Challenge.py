import random

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return f"Name: {self.name} | hp: {self.hp}"

    def take_damage(self, dmg):
        self.hp -= dmg
        print(f"{self.name} took {dmg} damage! {self.hp} hp remaining.")

class Warrior(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength

    def __str__(self):
        return f"{super().__str__()} | Strength: {self.strength}"

    def attack(self, weapon_base_dmg, enemy_hp):
        dmg = self.strength * weapon_base_dmg
        enemy_hp -= dmg
        print(f"The enemy takes {dmg} damage! The enemy has {enemy_hp} hp remaining.")

class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana
        
    def __str__(self):
        return f"{super().__str__()} | Mana: {self.mana}"

    def cast_spell(self, spell_type, mana_cost):
        self.mana -= mana_cost
        print(f"{self.name} cast a {spell_type} spell! {self.mana} mana remaining.")

player1 = Warrior("Clay", 50, 4)
player2 = Mage("Cole", 35, 25)

print(f"Start info:\n"
      f"{player1}\n"
      f"{player2}")

player1.take_damage(random.randint(4, 15))
player2.cast_spell("fireball", 12)
player1.attack(random.randint(5, 10), 40)
player2.take_damage(random.randint(4, 15))

print(f"End info:\n"
      f"{player1}\n"
      f"{player2}")