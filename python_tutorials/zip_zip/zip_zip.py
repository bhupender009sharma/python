num1 = [1,2,3,4,5,6]
num2 = [2,4,5,7,32,7]

num = zip(num1,num2)    # joins to list as follows
# [(1,2),(2,4),(3,5),...]
for a,b in num:
    print(a,b)