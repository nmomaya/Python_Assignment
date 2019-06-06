"""
WAP for factorial of a number

def factorial(no1):
    no2 = 1
    for i in range (1,no1):
        no2 = no2 * no1
    return(no2)

def recfact(no1):
    if (no1 == 0 or no1 == 1):
        return (1)
    else:
        return (no1*recfact(no1-1))

no1 = eval(input ("Please enter no1."))
no2 = recfact(no1)
print(no2)
"""
# This is called as stack frame


# WAP to accept 2 no.'s from user and find GCD

def GCD(no1, no2):
    while(no1 != no2):
        if (no1 > no2):
            no1 = no1 - no2
        else:
            no2 = no2 - no1
    return (no1)

# WAP to find GCB using recursive function

def recGCD(no1,no2):
    if (no1 > no2):
        return(no1 - no2)
    else:
        return()


no1,no2 = eval(input ("Please enter number:"))
no = recGCD(no1,no2)
print(no)


