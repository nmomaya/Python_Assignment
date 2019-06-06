
def IsPrime(no):
    import math
    if (no <0):
        no = no * -1
    if (no % 2 == 0):
        return False
    else:
        for x in range (3, int(math.sqrt(no))+1, 2):
            if no%x==0:
                return False
        return True



    def Ispalindrome(input_str):
    return input_str==input_str[::-1]

def main():

    no = input("Enter Number of range")
    if IsPrime(no):
        print ("Correct")
    else:
        print ("Not Correct")
   
if __name__ == "__main__":
    main()
