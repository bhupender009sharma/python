from operator import itemgetter
# itemgetter, similar to attribute getter
users = [
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Roberts'},
    {'fname': 'Bernie', 'lname': 'Zunks'},
    {'fname': 'Johnny', 'lname': 'Hayes'},
    {'fname': 'Johnny', 'lname': 'Concrete'},
    {'fname': 'Donald', 'lname': 'Pump'},
    {'fname': 'Ho-Lee', 'lname': 'Fuk'},
    {'fname': 'Johnny', 'lname': 'Nut'},
    {'fname': 'Jedediah', 'lname': 'Springfield'},
    {'fname': 'Super', 'lname': 'Mario'}
]
# you can get error , if you try to sort with same name but with CAPITAL or small letters
for x in sorted(users,key= itemgetter('fname')):
    print(x)

print('\nlook for lname with Johnny , it does not have their fname in sorted order , in above output \n')

for x in sorted(users,key= itemgetter('fname','lname')):
    print(x)