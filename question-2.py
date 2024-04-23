# Write a Python program to find whether a given number is even or odd, print out an #appropriate message to the user ?


n1 = int(input("Enter n1 : "))    # input number

# For Odd and Even numbers

if n1==0:
    print(n1, "is nither even nor odd")    # For neither even nor odd

elif n1%2==0:
    print(n1,"is even")       # For even numbers will print even 

else:
    print(n1,"is odd")       # For odd numbers will print odd



