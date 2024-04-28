# Write a Python function that takes a list of words and returns the length of the longest one.

def longestLength(words):
    str=max(words,key=len)       # To calculate the maximum length
    print("The word with the longest length is:", str,
          " and length is ", len(str))
 
 
a = ["one", "two", "third", "hundred"]    # Array of words
longestLength(a)

