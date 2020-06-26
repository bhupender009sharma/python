class Mario():
    def move(self):
        print("bitch i'm sliding")

class shroom():
    def eat_shroom(self):
        print("nigga i'm big!!! whoooo!")

class BigMario(Mario,shroom):
    pass                        # if you dont want to change anything in the function , but want to use functio like
                                # this one , but we will get syntax error , so we use pass , it helps us to overcome
                                # the syntax error
bg = BigMario()
bg.move()
bg.eat_shroom()