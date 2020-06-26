class Enemy:
    def __init__(self,x):       # init is called initialiser
        self.energy=x           # it will run firstly even if you called another function in the class

    def get_energy(self):
        print(self.energy)

bhola = Enemy(10)
kalsi = Enemy(50)

bhola.get_energy()
kalsi.get_energy()