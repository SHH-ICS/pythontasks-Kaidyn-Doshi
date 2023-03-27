# TASK: Update both functions to reverse the letters in the name and provide the square root of the users age.
import math
me = input("What is your name? ")
im = input("What is your age? ")
def reverseName(myName):
  result = myName
  return result[::-1]
def rootAge(myAge):
  myAge = math.sqrt(int(im))
  result = myAge
  return result
print("Your name in reverse is: ",reverseName(me))
print("The square root of your age is: ",rootAge(im))
