class girl:
    gender = 'female'           # class variable
    def __init__(self,name):
        self.name= name         # self.name  is an instance variable

b = girl('bhupini')
s = girl('saadhni')

print(b.name)
print(b.gender)
print(s.name)
print(s.gender)