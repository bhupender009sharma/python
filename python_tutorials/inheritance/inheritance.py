class parent():
    def last_name(self):
        print('sant')

class child(parent):            # here all the functions of the parent class are copied into the child class
    def first_name(self):       # this is called inheritance
        print('saadhu')

    # we can also modify the function defined in the parent, here last_name
   # def last_name(self):
    #    print('baba')

saadhu = child()
saadhu.first_name()
saadhu.last_name()