"""
def bit(no1):
    no2 = no1 & 1
    print(bin(no1))
    print(no2[-1])
    if no2 == 0:
        sum = sum + 1

if __name__ == '__main__':
    no1 = eval(input("Enter Number:"))
    bit(no1)

"""
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)