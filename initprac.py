#automatically will run without having to call it

class Tuna:

    def __init__(self): #this will run/initalize automatically. no need to call it
        print("asdfagasdfasdgasdf")

    def swim(self): #wont run automatically. we need to call this one
        print("I am swimmimmg")

flipper = Tuna()
flipper.swim()

class Enemy:
    def __init__(self, x):
        self.energy = x
    def get_energy(self):
        print(self.energy)

Syd = Enemy(5)
Teddy = Enemy(50)
Bella = Enemy(100)

Syd.get_energy()
Teddy.get_energy()
Bella.get_energy()
