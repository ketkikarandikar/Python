# Write a Python function to insert a string in the middle of a string ?

def insert_string_middle(str, word):
    # Create and return a new string by concatenating the first two characters of 'str',
    # followed by the 'word', and then the remaining characters of 'str' starting from the third character.
    return str[:2] + word + str[2:]

# Call the insert_string_middle function with different input strings and words and print the results.
print(insert_string_middle('[[]]', 'Python'))  # Output: '[Python]'
print(insert_string_middle('{{}}', 'PHP'))    # Output: '{{PHP}}'
print(insert_string_middle('<<>>', 'HTML'))    # Output: '<>'



