import os

class Weapon:
    def __init__(self):
        self.name = "AK47"

class Fighter:
    def __init__(self, n, v, w):
        self.nombre = n
        self.vida = v
        self.weapon = w.__dict__
        
    def attack():
        print("attacking, (visually)")

class Player(Fighter):
    def __init__(self, nombre, vida, w):
        super().__init__(nombre, vida, w)
        
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
    ak = Weapon()
    player = Player("Player 1", 100, ak)
    
    
    print(player.__dict__)
    return
    while True:
        os.system("clear")
        menu()
        action = input("Introduce tu action: ")
        
        
        if action == "1":
            print("This option is not valid at this time.")
            
        elif action == "3":
            print("leaving the program...")
            
    
    
if __name__ == "__main__":
    main()    
