#WAP to add all numbers divisible by 7 and 9 from 1 to n and n is given by the user.
n=int(input("Enter a number:"))
d=0
for i in range (1,n+1):
    if(i%7==0 and i%9==0):
        d+=i
print(d)        