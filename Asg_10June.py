"""
1. WAP to accept 2 numbers from user, accept position and number of bits to be swapped of the given numbers.
Hint:
I) Create 4 one bits number that is aligned to given number.
II) x_part = x & x_mask
     y_part = y & y_mask
III) turn off those 4 bits from x and y
IV) x = x I y_part
      y = y I x_part

2. WAP to accept two numbers and 2 positions and then swap it.  (same as above only positions are different)

"""
"""
def bitpost(no1,pos,digit):
    x = 1
    print(bin(no1))
    x = (1 << digit) -1
    print(x)
    x = x << (pos - digit)
    print(x)
    x =~x
    return(no1 & x)

no1,pos,digit = eval(input("Enter Number, Bit Position and Digit:"))
output = bitpost(no1,pos,digit)
print("Number is:",output)
"""
# 3. WAP to add 2 numbers without arithmetic operators. ( use bitwise operators)

def add(no1,no2):
    no3 = no1 ^ no2
    carry = no1 & no2
    if (carry != 0):
        return add(no3,carry << 1)
    return(no3)

no1,no2 = eval(input("Enter Numbers:"))
result = add(no1,no2)
print("Number is:",result)