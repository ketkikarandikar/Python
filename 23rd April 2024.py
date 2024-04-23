"""
for i in range(1, 6):
  for k in range(1, 6 - i):
    print(" ", end="")

  for j in range(i):
    print("*", end="")

  print()
"""
"""
for i in range(1, 7):
  print("* " * (7 - i))

for i in range(1, 7):
  print(" " * (7 - i), "* " * i)

for i in range(1, 7):
  print(" " * (7 - i), "*" * i)
"""
"""
k = "Tops Technologies"

print(len(k))  # to know length
print(type(k))  # to know wether it is string or other

print(k.capitalize)  # first letter capital
print(k.upper())  # all letter capital
print(k.lower())  # all letter small
print(k.islower())  # to check all letter small or not
print(k.isupper())  # to check all letter capital or not
print(k.casefold())  # to convert all letter small
print(k.swapcase())  # to convert all letter capital and capital letter small
print(k.title())  # to convert first letter capital
print(k.center(25, "!"))  # to center the string
print(k.count("e"))  # to count the letter
print(k.replace("o", "f"))  # to replace the letter
print(k.endswith("kd"))  # to check the string end with letter or not
print(k.isalpha())  # to check the string is alpha or not
print(k.count("o"))  # to count the letter
print(k.find("e"))  # to find the letter
print(k.index("o", 11))  # to find the letter

K1 = '-'.join(k)
print(K1)
"""

s = 'Tops Technologies'

print(s[3:12:2])

print(s[12:15])

print(s[11:15:2])

print(s[2::])

print(s[::3])

print(s[2::1])

print(s[:12:3])

