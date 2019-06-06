"""
no = 1
while(no != 0):
    no = eval((input("Enter no:0 to exit")))
    print("Entered no.:",no)

def strcount(str1):
    count = 0
    try:
        while (str1[count] != "\0"):
            count+=1
    except:
        pass
    return count
"""
def strcount(str1):
    count = 1
    while(str1[:1] != str1):
        count += 1

if __name__ == '__main__':
    str1 = eval(input("Enter the string"))
    count = strcount(str1)
    print("Count is",count)