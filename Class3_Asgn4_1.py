""" Date : 23rd-Dec-17 """
"""
India
aIndi
iaInd
iadIn
niadI


str1 = eval(input("Enter String: "))
print ("You entered: ",str1)
str2 = eval(input("Enter String: "))
print ("You entered: ",str2)
"""
str1 = "india"
str2 = "iaind"

if (len(str1) == len(str2)):
    str3 = str1 + str1
    print (str3)
    if (str3.__contains__(str2)):
        print("String %s is reverse order of string %s" % (str1, str2))
    else:
        print ("String %s is not a reverser order of %s"%(str1,str2))
else:
    print("Length is different of string %s and string %s"%(str1,str2))
