# Write a Python function to reverses a string if its length is a multiple of 4.

test_str = 'This book is for me myself '   # printing original string
print("The original string is : " + str(test_str))
test=test_str.split()
mid_str = "better"             # initializing mid string
mid_pos = len(test) // 2     # finding middle word
test.insert(mid_pos,mid_str)
print("Formulated String : " + str(" ".join(test)))



