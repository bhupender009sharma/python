while 1:
    try:                    # enter the code that you think possibly could give you an error
        num = int(input("enter any num\n"))
        print(77/num)
        break
    except ValueError:                  # error type that can occur
        print("enter int number only")
    except ZeroDivisionError :          # error type that can occur
        print('dividing by zero is not possible')
    except:                             # when you don't know anymore types of error that can occur
        break                           # try not use it , else you will not be able to know the source of error

    finally:                            # do this , no matter what
        print('loop completed')