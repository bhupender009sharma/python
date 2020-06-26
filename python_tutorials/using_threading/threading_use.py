import threading        #threading is a module

class saadhuMessenger(threading.Thread):        # here we have imported Thread class in here
    def run(self):          # run is a spicific type of function which is used in threading , it is not self made
        for _ in range(100): # _ can used as a variable as we use i, when we do not want to do anything with variable
            print(threading.currentThread().getName())

x= saadhuMessenger(name = "send message")  # we can give names to threads
y= saadhuMessenger(name= "recieve message")

# here we do not use  like x.run()

x.start()       # in threading we use start function
y.start()       #  in threading first x will start, then it will not wait to complete the all the functions of
                # but as soon as it gets to x , then it will start running y.start() and will not for x.start()
                # to finish first
