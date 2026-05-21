class Player:
    def __init__(self, name, life, points):
        self.__name = name
        self.__life = life
        self.__points = points
    
    def attack(self):
        return 30
    
    def set_points(self):
        self.__points += 30

    def get_points(self):
        return self.__points

class Enemy:
    def __init__(self, name, life):
        self.__name = name
        self.__life = life
    
    def take_damage(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0
    
    def get_life(self):
        return self.__life

player1 = Player("Josefino09", 100, 0)
enemy1 = Enemy("Enemigo", 100)

while True:
    print("\n1.- Attack enemy")
    print("2.- Exit")
    option = int(input("Choose one: "))

    match(option):
        case 1:
            damage = player1.attack()
            enemy1.take_damage(damage)
            print(f"Enemy life: {enemy1.get_life()}")
        case 2:
            break
    
    if enemy1.get_life() <= 0:
        print("\nYOU WIN")
        player1.set_points()
        print(f"TOTAL POINTS: {player1.get_points()}")
        break

