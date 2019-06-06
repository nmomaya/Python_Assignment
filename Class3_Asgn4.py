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
    i = len(str3)
    print (str3)
    print (str3[:i-1:1])
    print (str3[i-1])
    while (i != 0):

     if(str2 == (str3[i-1] + str3[:i-1:1])):
         print ("String %s is reverser order of %s"%(str3,str2))
     else:
        print ("String %s is not a reverser order of %s"%(str3,str2))
     i = i - 1

else:
    print("Length is different of string %s and string %s"%(str1,str2))
