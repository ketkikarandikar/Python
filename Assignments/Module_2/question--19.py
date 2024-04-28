# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

def not_poor(str1):
    # Find the index of the substring 'not' in the input string 'str1' and store it in 'snot'.
    snot = str1.find('not')
    
    # Find the index of the substring 'poor' in the input string 'str1' and store it in 'spoor'.
    spoor = str1.find('poor')

    # Check if 'poor' is found after 'not', and both 'not' and 'poor' are present in the string.
    if spoor > snot and snot > 0 and spoor > 0:
        # Replace the substring from 'snot' to 'spoor+4' (inclusive) with 'good'.
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        # If the conditions are not met, return the original 'str1'.
        return str1

# Call the not_poor function with different input strings and print the results.
print(not_poor('The lyrics is not that poor!'))  # Output: 'The lyrics is good!'
print(not_poor('The lyrics is poor!'))          # Output: 'The lyrics is poor!'
