#Write a Program in Python to detect whether given string are anagram or not

string=input("Enter string:")

if (string == string[::-1]):
    print("string is Anagram")
else:
    print("Not Anagram")
    
