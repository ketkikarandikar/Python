# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero ?

x = int(input("Enter number  1 :"))   # enter the numbers

y = int(input("Enter number 2 :"))

z = int(input("Enter number 3 :"))

if x == y or y == z or x == z:                # For equaling the numbers
    sum = 0     
else:
    sum = x+y+z                             # sum of 3 numbers

print(sum)