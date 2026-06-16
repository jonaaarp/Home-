import os
import random
import time
import json


def save_data(player):
    public = "/sdcard/Download/rpgconsole.json"
    data = player.__dict__.copy()
    
    for clave, valor in data.items():
        if hasattr(valor, '__dict__'):  # Si el atributo es otro objeto personalizado
            data[clave] = valor.__dict__ # Lo convertimos a diccionario básico
            
    
    with open(public, "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    pass
    
class GameState:
    MENU = 0
    START = 1


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
        
    def attack(self, life_enemy):
        print("has attacked with", self.weapon.name, "did", self.weapon.damage, "of damage")
        result = life_enemy - self.weapon.damage 
        return result
        
class Enemy(Fighter):
    def __init__(self, name, life, weapon, reward):
        super().__init__(name, life, weapon)
        self.reward = reward
    
class Player(Fighter):
    state = 0
    id_c = 1
    def __init__(self, name, life, weapon):
        super().__init__(name, life, weapon)
        
        self.id_player = Player.id_c
        self.admin = False
        self.gold = 0
        self.should_i_leaving = False
        self.wins = 0
        
    def leaving(self):
        self.should_i_leaving = not self.should_i_leaving
        
def profile(player: Player):
    os.system("clear")
    print("name:", player.name,
    "\nmoney:", player.gold,
    "\nweapon:", player.weapon.name)
    
def menu():
    print("press the option key\n")
    
    print("1. start")
    print("2. shop")
    print("3. settings")
    print("4. exit\n")

def create_enemy(weapons):
    enemy_id = random.randint(1, 100)
    life = random.randint(50, 100)
    arms = random.choice(weapons)
    gold_reward = random.randint(0, 100)
    return Enemy("BOT " + str(enemy_id), life, arms, gold_reward)
    
def menu_fight(player: Player, bot: Fighter):
    os.system("clear")
    print(player.name, 6 * " ", bot.name)
    print(10 * " ", "vs")
    print("life:",player.life, 5 * " ", "life:", bot.life)
    print("\n1. attack")
    print("your potions: ", end="")
    for potions in player.potion:
        print(potions, end=" - ")
    print("\n")    
    
    
    
def main():
    
    list_weapons = [
      Weapon("hand", 10, 0),
      Weapon("kitchen knife", 50, 50)]
      
    list_boss_bots = [
      Fighter("bot test", 100, list_weapons[0])
    ]
      
    player = Player("Player 1", 100, list_weapons[0])
    player.admin = True
    
    
    while not player.should_i_leaving:
        
        
        if player.state == GameState.MENU:
            profile(player)
            menu()
        
            action = input("Enter your action: ")
        
            if action == "1":
                player.state = GameState.START
                
            elif action == "3":
                print("leaving the program...")
                player.leaving()
                
        
        if player.state == GameState.START:
            # chosen_boss = random.choice(list_boss_bots)
            enemy = create_enemy(list_weapons)
            while player.life > 0:
                menu_fight(player, enemy)
                
                action = input("Write your action: ")
                
                
                if action == "info":
                    print(enemy.__dict__)
                    time.sleep(1.5)
                
                if action == "leave":
                    player.state = GameState.MENU
                    break
                    
                if enemy.life <= 0:
                    player.gold = player.gold + enemy.reward
                    player.wins = player.wins + 1
                    break
                        
                elif action == "1":
                    enemy.life = player.attack(enemy.life)
                    if player.admin == False:     
                        time.sleep(0.5)
                
                save_data(player)
                
                
                
if __name__ == "__main__":
    main()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
