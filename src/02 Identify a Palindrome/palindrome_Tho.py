"""
  Python Code Challenge #2: Identify a Palindrome
Your goal is to implement a function, is_palindrome(), that takes a text string as the input argument and returns a boolean indicating whether or not it's a palindrome.

Example Test Output
>>> is_palindrome('hello world')
False
>>> is_palindrome('Go hang a salami, I’m a lasagna hog.')
True
"""
import re

def is_palindrome(text):
  res = False
  letter = [x.lower() for x in text if not x in ("' ', ',', '.', '\"'")]
  for i in range(0, len(letter), 1):
    if letter[i] == letter[-(i+1)]:
      res = True
      continue
    else:
      res = False
      break
  return res

print(is_palindrome("Go hang a salami, I\"m a lasagna hog."))