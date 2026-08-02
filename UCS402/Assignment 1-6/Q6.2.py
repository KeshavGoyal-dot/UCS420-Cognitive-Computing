#WAP using function that add all prime numbers from 1 to n, n given by the user.
def isPrime(n):
    if n<2:
        return False
    for i in range (2,n):
        if(n%i==0):
            return False
    return True

def addPrime(n):
    sum=0
    for i in range(2,n+1):
        if isPrime(i):
            sum+=i
    print(sum)

n=int(input("Enter a number:"))
addPrime(n)                