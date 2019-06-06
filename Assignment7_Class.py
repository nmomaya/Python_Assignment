""" Write a program to accept a range from user and print all odd numbers in the same. Hint: Don't use any arithmatic operator.
Accept 2 vaules. Use bitwise. Do validation for upper & lower numbers """

def IsOdd(num):
    return ((num & 1) == 1)

""" return num%2 == 1 """

lb,ub = eval(input ("Please enter two number"))
print(lb,ub)

if (lb < ub):
    for x in range(lb,ub):
        if IsOdd(x):
            print("%d is odd number" %x)
       
else:
    print ("Incorrect range")
        

