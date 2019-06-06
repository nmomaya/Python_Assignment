"""
def update(str):
        result = {}
        firstlist = (str.split("\n"))
        for line in firstlist:
            if line.count(",") == 1:
               value =  line.split(",")
               result[value[0]] = value[1]
               print(value[0],value[1])
        return(result)

def main():
    str = "Software-Name,Test\nVersion,1.0\nPurpose,Education\n"
    result = update(str)
    print(result)
if __name__ == '__main__':
    main()

WAP to accept two list from user & creat a dictonory in which keys are from list1 and value from list 2

def listconcat(l1,l2):
    result = {}
    if (type(l1) == list and type(l2) == list):
        i = 0
        while i < len(l1):
            if i < len(l2):
                result[l1[i]] = l2[i]
            else:
                result[l1[i]] = None
            i += 1
    return(result)

def main():
    l1= [1,2]
    l2 = [4,5,6]
    result = listconcat(l1,l2)
    print(result)
if __name__ == '__main__':
    main()

"""
# WAP accept student details from User,Name,Email id, mobile no.,Crate a dictinory of Student where roll no is auto getated starting from 1 and it is key in result dictionary

def datarecord(n):


def main():
    n = print("Enter the number of Students to enter")
    datarecord(n)

if __name__ == '__main__':
    main()
