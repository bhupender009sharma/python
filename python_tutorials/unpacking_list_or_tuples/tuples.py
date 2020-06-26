name, line, num = ['saadhu ' ,'dob is ', 1999 ]
print(line)

def drop(grades):
    first , *middle , last= grades          #use *variable , it will store all the values of the list
    # first will have first value, middle will have all the values except first and last ,& last will have last value
    avg = sum(middle) / len(middle)
    print(avg)

drop([1,2,3,0])
