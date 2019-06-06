
# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(str1):
    if(len(str1) < 4):
        return (str1)
    elif ((str1[-3:]=="ing")):
        return(str1[:-3]+"ly")
    else:
        return(str1 + "ing")
           
                            
def main():
    
    str1 = eval(input("Enter strings: "))
    str3 = verbing(str1)
    print("Verbing form of %s string is %s"%(str1,str3))
if (__name__=='__main__'):
    main()

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    str1 = s.find("not")
    str2 = s.find("bad")
    s.contains
        
    print(s)

s = eval(input("Enter String: "))
not_bad(s)


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    if ((len(a)%2) == 0):
        ano = len(a) // 2
    else:
        ano = (len(a) // 2) + 1
    afront = a[0:ano]
    aback =  a[ano:]
    print(afront,aback)
    if ((len(b)%2) == 0):
        bno = len(b) // 2
    else:
        bno = (len(b) // 2) + 1
    bfront = b[0:bno]
    bback = b[bno:]
    print(bfront,bback)
    strfinal = afront + bfront + " " + aback + bback
    print("String is - {}".format(strfinal))
a,b = eval(input("Enter Two Strings: "))
front_back(a,b)

"""
