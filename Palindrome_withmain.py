""" Palindrome String """

def Ispalindrome(input_str):
    return input_str==input_str[::-1]

def main():

    input_str = input("Enter String")
    if Ispalindrome(input_str):
        print ("Correct")
    else:
        print ("Not Correct")
   
if __name__ == "__main__":
    main()
