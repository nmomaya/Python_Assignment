import re
def regularexpression(text):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search(text)
    print(mo.group(1))
    print('Phone number found: ' + mo.groups())

regularexpression("My number is 415-555-4242")