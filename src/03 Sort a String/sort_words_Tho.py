"""
Python Code Challenge #3: Sort a String
Your goal is to implement a function, sort_words(), that takes a string containing one or more words separated by spaces as the input argument and returns a string containing those words sorted alphabetically.

Example Test Output
>>> sort_words('banana ORANGE apple')
'apple banana ORANGE'

"""

def sort_words(text_string):
  text_list = text_string.split(" ")
  text_list.sort(key= lambda v: v.lower())
  return text_list

print(sort_words('banana ORANGE apple'))