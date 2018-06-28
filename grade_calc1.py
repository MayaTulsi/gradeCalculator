import os
# grade calculator second prototype bases on learning from first prototype


def user_input(n):      # function to take pieces of data from user with which to calculate final percentage.
    if n is 1:
        number_of_modules = (input("Please input the number of modules you wish to find the average of: "))
        mod_num = error_check(1, number_of_modules, int, 25, 1, 0)      # error check inputted value
        return mod_num              # return checked value to main function

    elif n is 2:
        grade = input("Please input your grade: ")
        checked_grade = error_check(2, grade, float, 100, 0, 0)
        return float(checked_grade)

    else:
        credit = input("How many credits was this module worth? ")
        checked_credit = error_check(3, credit, int, 50, 0, 5)
        return int(checked_credit)


def error_check(n, value, typ, maxx, minn, mod):     # various parameters used to test value for suitability
    try:
        truevalue = typ(value)     # if value is of the expected type it is assigned to the variable 'truevalue'

        if truevalue > maxx or truevalue <= minn:     # checks value is within specified size limitations (min, max)
            error_message(2, typ, minn, maxx)        # calls error function to print appropriate error message
            return user_input(n)        # user is asked for input of same information(n) again

        elif mod is not 0:              # only runs when mod is not 0, as only credit value requires this check
            if truevalue % 5 != 0:      # if value is not divisible by 5 error message function is called
                error_message(3, typ, minn, maxx)
                return user_input(n)    # user is asked for input of same information(n) again
            else:
                return truevalue    # if mod is divisible by 5 truevalue is returned this is used for calculation
        else:
            return truevalue        # if value is of the correct type and is within size limits truevalue is returned

    except ValueError:              # if type is not that which is expected error message is displayed
        error_message(1, typ, minn, maxx)
        return user_input(n)        # user is asked for input of same information(n) again


def error_message(n, typ, mi, ma):   # error messages used in error_check, to nudge user to input appropriate value
    if n is 1:
        print(" Value error please input data in the " + str(typ) + " format")
    elif n is 2:
        print("Please input a number between " + str(mi) + " and " + str(ma))
    elif n is 3:
        print("Credit value must be divisible by 5 (e.g. 5, 10, 15, 20)")


def main():
    os.system("cls")
    credit_tot = 0      # credit total set to 0
    alist = []          # empty list

    modulenumber = user_input(1)    # calls for first user input,
    for i in range(modulenumber):   # runs below code for number of modules specified in first input
        grade = user_input(2)
        cred = user_input(3)
        alist.append((grade/100)*cred)  # finds weighted grade depending on credit value and adds to list
        credit_tot += cred          # adds credit value to credit total, this is important for finding final average

    litotal = sum(alist)            # sum of weighted grade values in list
    res = litotal/credit_tot        # finds final weighted result
    print("Calculated working grade based on credits: " + "{:.2%}".format(res))  # prints to 2 decimal places


main()
