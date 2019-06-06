""" Write a program to accept string from user
print how many vovels and consonnts are present in that string.
hint: count no. """

def vowels(str1):
    count=0
    for i in str1:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        count=count+1
    return(count)


str1 = eval(input("Enter String: "))
result = vowels(str1)
print ("Vowels in string %s are %d"%(str1,result))



"""

str1 = eval(input("Enter String: "))
counts = {i:0 for i in 'aeiouAEIOU'}
for char in str1:
    if char in counts:
        counts[char] += 1
        print (counts)
for k,v in counts.items():
    print(k, v)
"""
