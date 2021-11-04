"""Define the function to accept two parameters. word for the input string and x for the second string we are searching for
Split the string into substrings based on the second input parameter
Count the number of instances the substring appeared in the first input string based on the split string
Return the result"""


def count_multi_chart_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)