"""
assumptions: 
  the program will be able to take in capital or lowercase letters, but will only
    print out uppercase
  the program will exit if invalid input is detected. invalid input includes:
    more than one character
    a non alphabetic character.
  each letter is one space before or after the other, unless the multiplier is changed
"""
import sys

SPACES_MULTIPLIER = 1
CHARACTER_START = 'A'

#create a letter diamond with A at the top
def letter_diamond(char):
  if(len(char) != 1):
    print('Invalid input detected, exiting...')
    return ''
  char = char.upper()

  if(ord(char) < ord(CHARACTER_START) or ord(char) > ord('Z')):
    print('Invalid input detected, exiting...')
    return ''

  num_spaces = ord(char) - ord(CHARACTER_START)  
  print(spaces(num_spaces) + CHARACTER_START)
  
  #print the top half of the diamond, not including the center
  for i in range(num_spaces-1, 0, -1):
    print(spaces(i) + get_prev(char, i), end="")
    print(get_mid_spaces(num_spaces, i) + get_prev(char, i))
  
  #print the bottom half of the diamond, including the center
  for i in range(0, num_spaces):
    print(spaces(i) + get_prev(char, i), end="")
    print(get_mid_spaces(num_spaces, i) + get_prev(char, i))
  
  print(spaces(num_spaces) + CHARACTER_START)

#return the number of spaces for the middle of the diamond based on
#  how many steps have already been taken as well as 
#  the size of the pyramid itself (as represented by the number of steps between A and the letter in question)
def get_mid_spaces(full, step):
  return spaces(((full-step)*2)-1) + spaces(SPACES_MULTIPLIER-1, mul=False)

#return the letter based on the input letter and the step variable
def get_prev(letter, step):
  return chr(ord(letter)-step)

#return a string with "num" number of spaces
def spaces(num, mul=True):
  string = ""
  if(mul):
    for x in range(num * SPACES_MULTIPLIER):
      string = string + " "
  else:
    for x in range(num):
      string = string + " "
  return string


letter_diamond(sys.argv[1])



