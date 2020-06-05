#Write a Program in Python tocheck whether a given no is prime or not

a =int(input("Enter the number :"))
k=0
for i in range(2,a//2+1):
    if(a%i == 0):
        k=k+1
if (k<=0):
    print("Number is Prime ")
else:
    print("Number is Not Prime")
