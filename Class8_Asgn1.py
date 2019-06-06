# Write a program to accept a sentence from user and print count of
# characters and words.

def count_string_word(input_sent):
    char = 0
    word = 1
    for i in input_sent:
      char = char+1
      if(i==' '):
            word = word+1
            char = char-1
    print("Number of characters {} and words {} in the given sentence".format(char,word))


input_sent= eval(input("Enter sentence:"))
count_string_word(input_sent)

