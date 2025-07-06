class Enemy:
    life = 3

    def attack(self): #self just tells python that each object is going to be unique so it needs to store data with each unique object. (Keep track of its own data) (each superhero needs their own info so self lets python remember what each hero has)
        print("Ouch!")
        self.life -= 1
    
    def checkLife(self):
        if self.life <= 0:
            print("I am dead.")
        else:
            print(f'{self.life} life left')

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()

