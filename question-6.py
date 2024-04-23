# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5 ?

x = int(input("Enter num1 : "))
y = int(input("Enter num2 : "))
                                               
if x==y or abs(x - y) == 5 or (x + y) == 5:    # abs an absolute value of any numeric value input as an argument to the function
    print("True")                              # print boolean i.e true or false
else:   
    print("False")