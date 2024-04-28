# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

def add_string(str1):
    # Get the length of the input string 'str1' and store it in the variable 'L1'.
    L1 = len(str1)

    # Check if the length of 'str1' is greater than 2 characters.
    if L1 > 2:
        # If the last three characters of 'str1' are 'ing', add 'ly' to the end.
        if str1[-5:] == 'ing':
            str1 += 'ly'
        else:
            # If the last three characters are not 'ing', add 'ing' to the end.
            str1 += 'ing'

    # Return the modified 'str1'.
    return str1

# Call the add_string function with different input strings and print the results.
print(add_string('ab'))      
print(add_string('abc'))     
print(add_string('string'))  