"""Define the function to accept three parameters, one string and two characters
find the starting index of our substring using the second input parameter
find the ending index of our substring using the third input parameter
If neither of the indices are -1, return the portion of the first input parameter string between the starting and ending indices (not including the starting and ending index)
If either of the indices are -1, that means the start or end of the substring didn’t exist in our string. Return the original string in this case."""

def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
    return(word[start_ind+1:end_ind])
  return word