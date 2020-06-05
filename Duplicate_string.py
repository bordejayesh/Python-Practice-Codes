#Write a Program in Python to check common letters  in Two input string

str1  = input("Enter first String:")
str2  = input("Enter second String:")
a   = list(set(str1)&set(str2))
print("\n\t\t Common letters are :")
for i in a:
    print(i)
