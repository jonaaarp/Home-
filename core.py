import os

class Weapon:
    def __init__(self, name, damage, price):
        self.name = name
        self.damage = damage
        self.price = price

class Fighter:
    def __init__(self, name, vida, weapon):
        self.name = name
        self.vida = vida
        self.weapon = weapon.__dict__
        
    def attack():
        print("attacking, (visually)")

class Player(Fighter):
    def __init__(self, name, vida, weapon):
        super().__init__(name, vida, weapon)
        
        self.gold = 0
        self.should_i_leaving = False
        
    def leaving(self):
        self.should_i_leaving = not self.should_i_leaving

def menu():
    print("press the option key\n")
    
    print("1. start")
    print("2. settings")
    print("2. exit\n")
  
    
    
    



def main():

    list_weapons = [
      Weapon("hand", 10, 0),
      Weapon("kitchen knife", 50, 50)]
      
    player = Player("Player 1", 100, list_weapons[0])
    
    
    # print(player.__dict__)
    
    while not player.should_i_leaving:
        os.system("clear")
        print(player.name,
        player.gold,
        player.weapon["name"])
        menu()
        action = input("Introduce tu action: ")
        
        
        if action == "1":
            print("This option is not valid at this time.")
            
        elif action == "3":
            print("leaving the program...")
            player.leaving()
            
    
    
if __name__ == "__main__":
    main()    
