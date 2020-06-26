# map is used for passing a variable through a function

income = [10,302,33]

def double_money(dollars):
    return dollars * 2

new_income = list( map (double_money, income) )          # or we have to use for loop for doing double for element of
print(new_income)                                        # the list