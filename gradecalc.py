def get_grade():
    # function which takes user input and returns the weighted grade depending on credit value
    inp = input("input your grade: ")
    try:
        grade = float(inp)
        if grade > 100 or grade <= 0:
            print(errormsg(1))
            return get_grade()

        else:
            credit = get_credits()  # Calls another function
            try:
                credit = int(credit)
            except TypeError:
                credit = get_credits()

            val = (grade / 100) * credit
            return val, credit

    except ValueError:
        print(errormsg(2))
        return get_grade()


def get_credits():
    # Method used to obtain module credit data and update credit count
    inp = input("input how many credits the module is worth: ")

    try:
        credit = int(inp)
        if credit > 50 or credit <= 0:
            print(errormsg(3))
            if credit % 5 != 0:
                print(errormsg(4))

            return get_credits()

        elif credit % 5 != 0:
            print(errormsg(4))
            return get_credits()
        else:
            return credit

    except ValueError:
        print(errormsg(5) + " " + errormsg(4))
        get_credits()

    except TypeError:
        get_credits()


def find_total(li, totcred):
    # Method which sums together grades and divides by credit total
    list_total = sum(li)
    try:
        total = list_total/totcred
        return total
    except ZeroDivisionError:
        print(errormsg(6))


def errormsg(n):
    # Error messages which may be implemented
    if n == 1:
        return "Error grade should be between 0-100%"
    elif n == 2:
        return "Error input but be in numerical format, do not include '%' or other special characters"
    elif n == 3:
        return "Error, module credit should be between 5 and 50"
    elif n == 4:
        return "Error module credit should be a whole number divisible by 5, eg 10, 15, 20"
    elif n == 5:
        return"Input Error, value entered must be numerical"
    elif n == 6:
        return "Zero Division error"


def main():
    # implementation of functions in logical order
    credit_total = 0
    alist = []
    len_inp = input("How many grades do you have? ")
    try:
        li_len = int(len_inp)
        for i in range(li_len):
            value, cred = get_grade()
            alist.append(value)
            credit_total += cred

    except ValueError:
        print(errormsg(5))
        main()

    fin = find_total(alist, credit_total)
    print("Calculated working grade based on credits: " + "{:.2%}".format(fin))  # outputs in XX.XX% format

    return 0


main()  # RUN
