

def mixstr(str1):
    str3 = (str1[:2] + str1[-2:])
    return(str3)


"""
    if str1.endswith("ly"):
        return(str1[:-2]+"ing")
    elif str1.endswith("ing"):
        return(str1[:-3]+"ly")
    else:
        return(str1)

  
    if ((str1[-3:] == "ing")):
        return (str1[:-3] + "ly")
    elif((str1[-2:] == "ly")):
        return (str1[:-2] + "ing")
    else:
        return(str1)
    """

def main():
    str1 = eval(input("Enter String: "))
    if len(str1) <= 4:
        print("String {} is of four character".format(str1))
    else:
        str3 = mixstr(str1)
    # print("Verbing form of %s string is %s" % (str1, str3))
        print("Verbing form of {1} string is {0}".format(str3,str1))

if (__name__ == '__main__'):
    main()



st1 = eval(input("Enter String: "))
st2 = st1[::-1]

if (st2 == st1):
    print("String %s is Palindrome"%(st1))
else:
    print("String %s is not Palindrome"%(st1))