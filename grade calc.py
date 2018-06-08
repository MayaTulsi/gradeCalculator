
def getGrade():
    """METHOD TO GET INPUT FROM USER, TEST INPUT AND APPLY MATH TO FIND AMOUNT OF CREDITS GAINED PER MODULE"""
    grade = float(input("input your grade: "))

    if isinstance(grade,float)==False:
        print(errormsg(2))
        return False
    elif grade > 100:
        print(errormsg(1))
        return False
    else:
        credit= getCredits() #CALLS ANOTHER FUNCTION
        val=(grade/100)*credit
        return (val)
    
    
def getCredits():
    """METHOD USED TO OBTAIN MODULE CREDIT INFO AND UPDATE GLOBAL CREDIT COUNT"""
    credit = int(input("input how many credits the module is worth: "))
    if credit > 50:
        print(errormsg(3))
        return False
    elif isinstance(credit,int)==False :
        print(errormsg(4))
        return False
    elif credit/5!=0:
        print(errormsg(4))
        return False
    else:
        global creditTotal #GLOBAL VARIABLE USE, BAD PRACTISE BUT WORKS
        creditTotal +=credit
        return credit


def getGrade():
    """METHOD TO GET INPUT FROM USER, TEST INPUT AND APPLY MATH TO FIND AMOUNT OF CREDITS GAINED PER MODULE"""
    grade = float(input("input your grade: "))
    
    if grade > 100:
        print(errormsg(1))
    elif isinstance(grade,float)==False :
        print(errormsg(2))
    else:
        credit= getCredits() #CALLS ANOTHER FUNCTION
        val=(grade/100)*credit
        return (val)
    
    
def getCredits():
    """METHOD USED TO OBTAIN MODULE CREDIT INFO AND UPDATE GLOBAL CREDIT COUNT"""
    credit = int(input("input how many credits the module is worth: "))
    if credit > 50:
        print(errormsg(3))
    elif isinstance(credit,int)==False :
        print(errormsg(4))
    else:
        global creditTotal #GLOBAL VARIABLE USE, BAD PRACTISE BUT WORKS
        creditTotal +=credit
        return credit


def findTotal(list):
    """METHOD WHICH SUMS TOGETHER THE GRADE VALUES DERIVED IN GET GRADE AND DIVIDES BY GLOBAL CREDIT TOTAL"""
    listTotal=sum(alist)
    global creditTotal #GLOBAL VARIABLE
    total=round((listTotal/creditTotal),2)
    
    return(total)

def errormsg(n):
    """VARIOUS POSSIBLE ERRORS (INPUT ERRORS)"""
    if n ==1:
        return("Error grade but be between 0-100")
    elif n ==2:
        return("Error input but be in numerical format, do not include '%' or other special characters")
    elif n ==3:
        return("Error, module credit is never higher than 50")
    elif n ==4:
        return("Error module credit should be a whole number divisible by 5")

def main():
    """FUNCTION HAS BASIC IMPLEMENTATION OF GET GRADES AND OTHER FUNCTIONS RUN IN A LOGICAL ORDER, OUTPUTS FINAL VALUE"""
    liLen= int(input("how many grades do you have?"))
    for i in range (liLen):
        value = getGrade()
        alist.append(value)

    fin=findTotal(alist)
    print ("calculated working grade based on credits: "+"{:.2%}".format(fin))#OUTPUTS INFORMATION IN '100.00%' FORMAT
    return 0

alist=[] #GLOBAL VARIABLE
creditTotal=0 #GLOBAL VARIABLE

main()    #RUN

"""def findTotal(list):
    #METHOD WHICH SUMS TOGETHER THE GRADE VALUES DERIVED IN GET GRADE AND DIVIDES BY GLOBAL CREDIT TOTAL
    listTotal=sum(alist)
    global creditTotal #GLOBAL VARIABLE
    total=round((listTotal/creditTotal),2)
    
    return(total)

def errormsg(n):
    #VARIOUS POSSIBLE ERRORS (INPUT ERRORS)
    if n ==1:
        return("Error grade but be between 0-100")
    elif n ==2:
        return("Error input but be in numerical format, do not include '%' or other special characters")
    elif n ==3:
        return("Error, module credit is never higher than 50")
    elif n ==4:
        return("Error module credit should be a whole number divisible by 5")
    elif n ==5:
        return("Zero value removed from list")

def main():
    #FUNCTION HAS BASIC IMPLEMENTATION OF GET GRADES AND OTHER FUNCTIONS RUN IN A LOGICAL ORDER, OUTPUTS FINAL VALUE
    liLen= int(input("how many grades do you have?"))
    for i in range (liLen):
        value = getGrade()
        if value > 0:
            alist.append(value)
        else:
            errormsg(4)

    fin=findTotal(alist)
    print ("calculated working grade based on credits: "+"{:.2%}".format(fin))#OUTPUTS INFORMATION IN '100.00%' FORMAT
    return 0

alist=[] #GLOBAL VARIABLE
creditTotal=0 #GLOBAL VARIABLE

main()    #RUN
print (alist)"""
