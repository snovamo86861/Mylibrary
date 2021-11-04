"""3. Reverse
This one is similar to the last challenge. Instead of selecting every other letter, we want to reverse the entire string. This can be performed in a similar manner, but we will need to modify the range we are using. Here is what we need to do:

Define the function to accept one parameter for the string
Create a new empty string to hold the reversed string
Loop through the input string by starting at the end, and working towards the beginning
Inside the loop, append the character at the current location to the new string we initialized earlier
Return the result"""

def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse