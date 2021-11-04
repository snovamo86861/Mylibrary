"""2. Every Other Letter
For this next function, we are going to create a function that extract every other letter from a string and returns the resulting string. There are a few different ways you can solve this problem Here are the steps needed for one of the ways:

Define the function to accept one parameter for the string
Create a new empty string to hold every other letter from the input string
Loop through the input string while incrementing by two every time
Inside the loop, append the character at the current location to the new string we initialized earlier
Return the new string"""

def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other