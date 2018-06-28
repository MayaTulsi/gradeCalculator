# import os
# grade calculator second prototype bases on learning from first prototype

def user_input(n):
    if n is 1:
        number_of_modules = (input("Please input the number of modules you wish to find the average of: "))
        mod_num = error_check(1, number_of_modules, int, 25, 1, 0)
        return mod_num

    elif n is 2:
        grade = input("Please input your grade: ")
        checked_grade = error_check(2, grade, float, 100, 0, 0)
        return float(checked_grade)

    else:
        credit = input("How many credits was this module worth? ")
        checked_credit = error_check(3, credit, int, 50, 0, 5)
        return int(checked_credit)


def error_check(n, value, type, max, min, mod):
    try:
        truevalue = type(value)

        if truevalue > max or truevalue <= min:
            error_message(2, type, min, max)
            return user_input(n)

        elif mod is not 0:
            if truevalue % 5 != 0:
                error_message(3, type, min, max)
                return user_input(n)
            
        else:
            return truevalue

    except ValueError:
        error_message(1, type, min, max)
        return user_input(n)



def error_message(n,typ,min,max):
    if n is 1:
        print(" Value error please input data in the " + str(typ) + " format")
    elif n is 2:
        print("Please input a number between " + str(min) + " and " + str(max))
    elif n is 3:
        print("Credit value must be divisible by 5 (e.g. 5, 10, 15, 20)")


def main():
    credit_tot = 0
    alist = []

    modulenumber = user_input(1)
    for i in range(modulenumber):
        grade = user_input(2)
        cred = user_input(3)
        alist.append((grade/100)*cred)
        credit_tot += cred

    litotal = sum(alist)
    res = litotal/credit_tot
    print("Calculated working grade based on credits: " + "{:.2%}".format(res))

main()