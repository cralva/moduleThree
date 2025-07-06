class Enemy:
    life = 3
    def attack(self):
        print("OUCH")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("You are dead")
        else:
            print(f'{self.life} lives remaining')

enemy1 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()