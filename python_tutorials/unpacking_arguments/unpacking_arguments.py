def age_to_live( monfap ,weekly_exer,daily_water):
    age=80-(7*monfap)+(2*weekly_exer)+(1.25*daily_water)
    print(age)

bhupi=[0,5,5]
age_to_live(bhupi[0],bhupi[1],bhupi[2])
age_to_live(*bhupi)
dushman=[3,4,3]
age_to_live(*dushman)