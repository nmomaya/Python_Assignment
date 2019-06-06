
# 3. WAP to add 2 numbers without arithmetic operators. ( use bitwise operators)
"""
def add(no1,no2):
    for i in range(1,len(no1)):
        if (no1[i] != no2 [i]):
            return(False)
            break
        else:
            continue
    return True

no1 = [eval(input("Enter Numbers:"))]
no2 = [eval(input("Enter Numbers:"))]
result = add(no1,no2)
print("Number is:",result)
"""
#WAP to wrtie your own append function an given poistion
"""
def append1(no1,pos,digit):
    no3 = no1[:pos]
    no3.append[digit]
    no3 = no3 + no1[pos:]
    print(no3)

def append(no1,pos,digit):
    return no1[:pos] + [digit]+ no1[pos:]

no1 = [eval(input("Enter Numbers:"))]
pos, digit = eval(input("Enter position and digit"))
result = append(no1,pos,digit)
print(result)

"""
#WAP to find the index at any given position
"""
def pos(l1,index):
    print(l1)
    for i in range (0,len(l1)):
        if (index == l1[i]):
            print("Poistion is",i)
        else:
            continue
l1 = []
l1 = eval(input("Enter Numbers:"))
index = eval(input("Enter Digit"))
pos(l1,index)
"""
#WAP to short it using our own short method
"""
def sortlist(l2):
    for i in range (0,len(l2)):
        for j in range (0,len(l2)-i-1):
            if l2[j] > l2[j+1]:

                no = l2[j]
                l2[j] = l2[j+1]
                l2[j+1] = no
    print(l2)

l2 = eval(input("Enter Numbers:"))
sortlist(l2)
"""
# WAP to accept two list sort them using bubble sort method and merge them in separate list in sorted order
"""
def sortlist(l2):
    for i in range (0,len(l2)):
        for j in range (0,len(l2)-i-1):
            if l2[j] > l2[j+1]:
                no = l2[j]
                l2[j] = l2[j+1]
                l2[j+1] = no
    return(l2)

def merge(l3,l4):
    l5 = []
    i,j = 0
    while i < len(l3) and j < len(j):
        if l3[i] < l4[j]:
            l5.append(l3[i])
            i += 1
        else:
            l5.append(l4[j])
            j += 1
    if i < len(l3):
        l5.extend(l1[i:])
    if j < len(l4):
        l5.extend(l4[j:])

    #l5.extend(l3)
    #l5.extend(l4)
    #l5 = l3 + l4
    #sortlist(l5)
    return(l5)

#l1 = eval(input("Enter Numbers:"))
#l2 = eval(input("Enter Numbers:"))
l1 = [1,89,3]
l2 = [2,72,707,4]
l3 = sortlist(l1)
l4 = sortlist(l2)
print("Shorted List is:",l3)
print("Shorted List is:",l4)
l5 = merge(l3,l4)
print("Merged and sorted list is",l5)

# WAP to accept two list and return intersection of them

def Intersection(l1, l2):
    l5 = []
    for i in (l1):
        if (i == l2):
                l5.append(i)
    return(l5)
    #return (set(l1) & set(l2))

def union (l1,l2):
    
    for j in range (0,len(l1)-1):
        if (l1[j] == l1[j+1])
            l1.remove(l1[j])
    l5 = l1
    for i in (l2):
        if i not in l5
                l5.append(i)
    return(l5)
    
    return(set(l1) | set(l2))

l1 = eval(input("Enter Numbers:"))
l2 = eval(input("Enter Numbers:"))
l3 = []
l4 = []
print(Intersection(l1,l2))
print(union(l1,l2))

"""
# WAP to accept hydrogenous nested list and make it a single level list

def singlelist(l1):
    l3= []
    for i in (l1):
        if type(i) is list:
            singlelist(i)
        else:
            l3.append(i)
    print(l3)
 # l1 = eval(input("Enter Numbers:"))
l1 = [[1,2,[7,8,9]],4,5,6]
singlelist(l1)
