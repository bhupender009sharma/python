class Enemy:
    life = 3

    def attack(self):
        print("aaaa")
        self.life-=1

    def life_check(self):
        if self.life>0:
            print(self.life, 'life left')
        else:
            print("sended to valhalla")

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.life_check()
enemy2.life_check()