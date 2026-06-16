import os
import random



class Game_state:
    MENU = 0
    GAME = 1


class Weapon:
    def __init__(self, name, damage, price):
        self.name = name
        self.damage = damage
        self.price = price

class Fighter:
    def __init__(self, name, life, weapon):
        self.name = name
        self.life = life
        self.weapon = weapon
        self.potion = []
        
    def attack(self):
        print("attacking, (visually)")

class Player(Fighter):
    state = 0
    def __init__(self, name, life, weapon):
        super().__init__(name, life, weapon)
        
        self.gold = 0
        self.should_i_leaving = False
        
    def leaving(self):
        self.should_i_leaving = not self.should_i_leaving

def menu():
    print("press the option key\n")
    
    print("1. start")
    print("2. shop")
    print("3. settings")
    print("4. exit\n")


def menu_fight(player: Player, bot: Fighter):
    os.system("clear")
    print(player.name, 6 * " ", bot.name)
    print(10 * " ", "vs")
    print("life:",player.life, 5 * " ", "life:", bot.life)
    print("\n1. attack")
    print("your potions: ", end="")
    for potions in player.potion:
        print(potions, end=" - ")
    input()
    
def main():
    
    list_weapons = [
      Weapon("hand", 10, 0),
      Weapon("kitchen knife", 50, 50)]
      
    list_bots = [
      Fighter("bot test", 100, list_weapons[0])
    ]
      
    player = Player("Player 1", 100, list_weapons[0])
    
    while not player.should_i_leaving:
        os.system("clear")
        print("name:", player.name,
        "\nmoney:", player.gold,
        "\nweapon:", player.weapon.name)
        
        if player.state == Game_state.MENU:
            menu()
        
            action = input("Enter your action: ")
        
            if action == "1":
                player.state = Game_state.GAME
                
            elif action == "3":
                print("leaving the program...")
                player.leaving()
                
        
        if player.state == Game_state.GAME:
            chosen_enemy = random.choice(list_bots)
            menu_fight(player, chosen_enemy)
        
            
            
if __name__ == "__main__":
    main()    
