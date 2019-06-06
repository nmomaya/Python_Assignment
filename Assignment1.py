inp = "This is a Phython Class"
result = {}
for char in list(inp):
    if char == " ":
        continue
    elif result.has_key(char):
         result[char] = result [char] + 1
    else:
        result[char] = 1
print (result)



