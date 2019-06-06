"""
Pattern Alphabet
    A
    A B
    A B C 
    A B C D
"""
def alphabet1(raw):
    
# outer loop to handle number of rows
    for i in range(0,raw):
    # inner loop to handle number of columns
        num = 65
        for j in range(0, i+1):
            #print(chr(num), end=" ")
            print(chr(num+j), end=" ")
            #num = num + 1 we can print using %c
        print("\r")


# ord is used to convert ASCII value 

"""
Pattern Alphabet
      A
    B A B
  C B A B C 
D C B A B C D
"""
def alphabet2(raw):

        print("not done")




raw = eval(input ("Please enter raw's"))
alphabet1(raw)
alphabet2(raw)
