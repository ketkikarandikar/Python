"""
i = 1  # Inisialization
while (i <= 10):  # condition
  print(i)
  i += 1  #increment
"""

"""

for i in range(1,16,1):
  print(i)
  """
"""
i = 1
evcount = 0
evsum = 0
odcount = 0
odsum = 0
while(i<=5):
  n = eval(input("Enter Number : "))
  if (n%2==0):
    print(n, "is even")
    evcount+=1
    evsum+=n
  else:
    print(n, "is odd")
    odcount+=1
    odsum+=n

i+=1


print("Odd numbers are : ",odcount)
print("Even numbers are : ",evcount)
print("Odd numbers sum are : ",odsum)
print("Even numbers sum are : ",evsum)

"""
i = 1
evcount = 0
evsum = 0
odcount = 0
odsum = 0

for i in range(1, 6, 1):
   n = eval(input("Enter Number : "))
   if (n % 2 == 0):
     print(n, "is even")
     evcount += 1
     evsum += n
   else:
     print(n, "is odd")
     odcount += 1
     odsum += n
     
     
print("Odd numbers are : ", odcount)
print("Even numbers are : ", evcount)
print("Odd numbers sum are : ", odsum)
print("Even numbers sum are : ", evsum)



