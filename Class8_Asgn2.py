""" Write a program to accept a string from user, if length of the string is 3 charters or more,
-  than add ing to its end
-  if already has "ing" replace “ing” with "ly"
-  if length of string is less than 3 return same string """

def mixstr(str1):
    if(len(str1) < 4):
        return (str1)
    elif ((str1[-3:]=="ing")):
        return(str1[:-3]+"ly")
    else:
        return(str1 + "ing")
           
                            
def main():
    
    str1 = eval(input("Enter strings: "))
    str3 = mixstr(str1)
    print("Verbing form of %s string is %s"%(str1,str3))
if (__name__=='__main__'):
    main()    
    

   


