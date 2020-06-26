def datting_age(age):
    girls_age= age/2 +7
    return girls_age

for i in range(15,33):
    guy_limit=datting_age(i)
    print("guys aged",i,"can date girls of age", guy_limit,"or older")