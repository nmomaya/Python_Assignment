""" pattern
    *
  * *
* * *
"""

def raws(n):
# outer loop to handle number of rows
    for i in range(1,n+1):
    # inner loop to handle number of columns
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        print("")

    
n = eval(input ("Please enter raw's"))
raws(n)



""" pattern
    *
   * *
  * * *
 * * * * 
"""

def raws(n):
# outer loop to handle number of rows
    for i in range(1,n+1):
    # inner loop to handle number of columns
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(i):
            print(" * ",end=" ")
        print("")

    
n = eval(input ("Please enter raw's"))
raws(n)

""" pattern
    *
  * * *
* * * * *
"""

def raws(n):
# outer loop to handle number of rows
    for i in range(1,n+1):
    # inner loop to handle number of columns
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(i):
            print(" * ",end=" ")
        print("")

    
n = eval(input ("Please enter raw's"))
raws(n)

