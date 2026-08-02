#WAP to add all prime numbers from 1 to n and n is given by the user.
n=float(input("Enter a number:"))
sum=0
for i in range (2,(n/2)+1):
    if(n%i!=0):
        sum+=i
print(sum)        