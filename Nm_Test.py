""""
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
    ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)
"""
import random
messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])

'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])


'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])