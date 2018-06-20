def get_grade():
    # function which takes user input and returns the weighted grade depending on credit value
    inp = input("input your grade: ")
    try:
        grade = float(inp)

    except ValueError:
        print(errormsg(2))
        return get_grade()

    if grade > 100 or grade <= 0:
        print(errormsg(1))
        return get_grade()

    else:
        credit = get_credits()  # Calls another function
        val = (grade / 100) * credit
        return val


def get_credits():
    # Method used to obtain module credit data and update credit count
    inp = input("input how many credits the module is worth: ")

    try:
        credit = int(inp)
        if credit > 50:
            print(errormsg(3))
            return get_credits()

        elif credit % 5 != 0:
            print(errormsg(4))
            return get_credits()
        else:
            global creditTotal  # GLOBAL VARIABLE USE, BAD PRACTISE BUT WORKS
            creditTotal += credit
            return credit
    except ValueError:
        print(errormsg(4))
        get_credits()


def find_total(li):
    # Method which sums together grades and divides by credit total
    list_total = sum(li)
    global creditTotal  # GLOBAL VARIABLE
    total = list_total/creditTotal

    return total


def errormsg(n):
    # Error messages which may be implemented
    if n == 1:
        return "Error grade should be between 0-100%"
    elif n == 2:
        return "Error input but be in numerical format, do not include '%' or other special characters"
    elif n == 3:
        return "Error, module credit is never higher than 50"
    elif n == 4:
        return "Error module credit should be a whole number divisible by 5"


def main():
    # implementation of functions in logical order
    li_len = int(input("how many grades do you have? "))
    for i in range(li_len):
        value = get_grade()
        alist.append(value)

    fin = find_total(alist)
    print(
        "calculated working grade based on credits: " + "{:.2%}".format(fin))  # outputs in XX.XX% format
    return 0


alist = []  # GLOBAL VARIABLE
creditTotal = 0  # GLOBAL VARIABLE

main()  # RUN
