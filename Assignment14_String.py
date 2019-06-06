""" Write a program to accept 2 strings from user and
swap 1st 2 characters of each of them. """
def mixstr(str1,str2):
    str3 = str2[:2]+str1[2:]
    str4 = str1[:2]+str2[2:]
    print ("Result of String:%s is String:%s \n Result of String:%s is String:%s" %(str1,str3,str2,str4))

str1,str2 = eval(input("Enter two strings: "))
mixstr(str1,str2)


    

