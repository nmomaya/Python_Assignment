"""
# Write a program which accepts heterogeneous variable number of arguments and returns sum of integers from the argument list. Hint: type function.

def sumint(*args):
    sum = 0
    for x in args:

        # if type(x) is int:
        if isinstance(x,int):
            print(type(x))
            sum += x
    print("Number of integars {} in total {}".format((sum),len(args)))
# sec = [1,2,3]
sumint(10,"nm",45,"VB",[1,2,3])

"""
#Write a program to accept a number form user and display odd digits and even digits sum. No arithmetic operators to be used. Hint Bitwise Operator.
"""
def oddevendigit(no1):
    oddsum = 0
    evensum = 0
    while (no1 != 0):
        rem = no1 % 10
        if (rem & 1 == 1):
            oddsum += rem
        else:
            evensum += rem
        no1 =int(no1/10)
    return(oddsum,evensum)

def main():
    no1 = eval(input("EnterNumber:"))
    oddsum,evensum = oddevendigit(no1)
    print("Odd Sum is",oddsum)
    print("Even Sum is:",evensum)

if __name__ == "__main__":
    main()

"""
# Write a program to count of 1's bit in the given number

"""
def total(no1):
    print(bin(no1))
    count = 0
    x = 1
    y = -1
    while (y & no1 == 0):
        if (x & no1)!= 0:
            count +=1
        x = x << 1
        y = y << 1
    return(count)

no1 = eval(input("EnterNumber:"))
count = total(no1)
print("Count is",count)
"""
# Write a program to count of 0's bit in the given number
"""
def total(no1):
    print(bin(no1))
    count = 0
    x = 1
    y = 0
    while (y <= 64):
        if (x & no1)!= 1:
            count +=1
        x = x << 1
        y += y
    return(count)

no1 = eval(input("EnterNumber:"))
count = total(no1)
print("Count is",count)
"""
# Write a program to accept number from user and chk it is divisible by 8 and 64(use bitwise operator)

"""
def divisible(no1):
    print(bin(no1))
    #if(no1 & 7) == 0:
    #    print("Number is Divisible by 8")
    if(no1 & 63) == 0:
        print("Number is Divisible by 64")
    else:
        print("Number is not Divisible by 8 and 64")

no1 = eval(input("EnterNumber:"))
divisible(no1)

"""

# Write a program to accept number from user accept bit position which should be turned off

"""
def bitpost(no1,pos):
    print(bin(no1))
    x = 1 << (pos -1)
    print(x)
    x =~ x
    print(x)
    return(no1 & x)

no1,bp = eval(input("Enter Number and Bit Position"))
output = bitpost(no1,bp)
print("Number is:",output)
"""
# Write a program to accept number from user accept bit posi which should be turned off

# WAP to accept two numbers and 2 positions and then swap it.  (same as above only positions are different)

def swapbit(x,y,pos1,pos2,digit):
    xmask = (1 << digit) - 1
    xmask = xmask << (pos1 - digit)
    xpart = x & xmask
    x = x &(~xmask)

    ymask = (1 << digit) - 1
    ymask = ymask << (pos2 - digit)
    ypart = y & ymask
    y = y & (~ymask)

    if pos1 - pos2 > 0:
        xpart = xpart >> (pos1 - pos2)
        ypart = ypart << (pos1 - pos2)
    else:
        xpart = xpart << (pos2 - pos1)
        ypart = ypart >> (pos2 - pos1)
    x = x | ypart
    y = y | xpart
    return(x,y)

x,y,pos1,pos2,digit = eval(input("No1 ,No2, Position for no1,postion or no2 and Digit:"))
no1,no2 = swapbit(x,y,pos1,pos2,digit)
print("Numbers are:",no1,no2)