""" Write a program to accept a string from user and display a string made of 1st two & last two character.
Alternate characters. Hint: display alternate character starting with 1. """

def mixstr(str1,str2):
    if (chr in str2):
        str3 = str1[2:]+str2[:2]
    print ("Result of String:%s"(str3))

str1,str2 = eval(input("Enter two strings: "))
mixstr(str1,str2)
