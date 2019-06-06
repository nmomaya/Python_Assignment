# Write a program to display following patters. No. of rows.
"""
1st Pattern
    *
    * *
    * * *
    * * * *
"""
def pattern1(raw):

# outer loop to handle number of rows
    for i in range(0,raw):
    # inner loop to handle number of columns
        for j in range(0,i+1):
            print("*",end=" ")
        # ending line after each row
        print("\r")

"""
    2nd pattern    
    * * * *
    * * *
    * * 
    *
"""
def pattern2(raw):

# outer loop to handle number of rows
    for i in range(0,raw):
        # inner loop to handle number of columns
        for j in range(raw,i,-1):
            print("*",end=" ")
            # ending line after each row
        print("\r")

"""

3rd pattern

    *
   * *
  * * *
 * * * *  

"""
def pattern3(raw):

# outer loop to handle number of rows
    k = 2*raw - 2
    for i in range(0,raw):
        # inner loop to handle number of columns
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

"""
4th pattern
    *
   * *
  * * *
 * * * *  
  * * *
   * *
    * 
"""
def pattern4(raw):

    for i in range(raw+1):
        print(" "*(raw-i)+"* "*(i))
    for j in range(raw-1,0,-1):
        print(" "*(raw-j)+"* "*(j))
    print("\r")

"""

5th pattern

    *
  * * *
* * * * *  

"""
def pattern5(raw):
    for i in range(1,raw+1,2):
        print(" "*(raw-i)+"* "*(i))
        
"""

6th pattern

 * * * * * * * 
 * * *   * * * 
 * *       * *  
 *           * 

"""

def pattern6(raw):

# outer loop to handle number of rows
    for i in range(0,raw):
        # inner loop to handle number of columns
        for j in range(raw,i,-1):
            print("*",end=" ")
            # ending line after each row
        print("\r")


raw = eval(input ("Please enter raw's"))
pattern1(raw)
pattern2(raw)
pattern3(raw)
pattern4(raw)
pattern5(raw)
pattern5(raw)


