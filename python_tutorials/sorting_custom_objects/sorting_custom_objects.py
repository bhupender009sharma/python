from operator import attrgetter
# similar to itemgetter

class drop():

    def __int__(self,x,y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + ":" + str(self.user_id)          # as user_id can be in numbers

users = [
    drop('bhupi', 323),
    drop('rocky', 30),
    drop('saadhu', 878),
    drop('baba', 567),
    drop('bhola', 77),
    drop('shiv', 90)
]

for user in users:
    print(user)
                        # if we have not created __repr__ then it would have not known , what to print about user ,
                        # its name or its income, so it helps to get the detail or anything about the user , in any
                        # fashion we wnat
print("---------------")
for user in sorted(users, key= attrgetter('name')):
    print(user)

print("---------------")

for user in sorted(users, key= attrgetter('name')):
    print(user)