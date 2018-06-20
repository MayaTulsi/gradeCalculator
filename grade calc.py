def get_grade():
    # function which takes user input and returns the weighted grade depending on credit value
    grade = float(input("input your grade: "))

    if not isinstance(grade, float):
        print(errormsg(2))
        return False
    elif grade > 100:
        print(errormsg(1))
        return False
    else:
        credit = get_credits()  # Calls another function
        val = (grade / 100) * credit
        return val


def get_credits():
    # Method used to obtain module credit data and update credit count
    credit = int(input("input how many credits the module is worth: "))
    if credit > 50:
        print(errormsg(3))
        return False
    elif not isinstance(credit, int):
        print(errormsg(4))
        return False
    elif credit % 5 != 0:
        print(errormsg(4))
        return False
    else:
        global creditTotal  # GLOBAL VARIABLE USE, BAD PRACTISE BUT WORKS
        creditTotal += credit
        return credit


def find_total(li):
    # Method which sums together grades and divides by credit total
    list_total = sum(li)
    global creditTotal  # GLOBAL VARIABLE
    total = round((list_total / creditTotal), 2)

    return total


def errormsg(n):
    # Error messages which may be implemented
    if n == 1:
        return "Error grade but be between 0-100"
    elif n == 2:
        return "Error input but be in numerical format, do not include '%' or other special characters"
    elif n == 3:
        return "Error, module credit is never higher than 50"
    elif n == 4:
        return "Error module credit should be a whole number divisible by 5"


def main():
    # implementation of functions in logical order
    li_len = int(input("how many grades do you have?"))
    for i in range(li_len):
        value = get_grade()
        alist.append(value)

    fin = find_total(alist)
    print(
        "calculated working grade based on credits: " + "{:.2%}".format(fin))  # OUTPUTS INFORMATION IN '100.00%' FORMAT
    return 0


alist = []  # GLOBAL VARIABLE
creditTotal = 0  # GLOBAL VARIABLE

main()  # RUN
