def mul(*args):
    total=1
    for i in args:
        total*=i
    print(total)

mul(3)
mul(3,5,6)