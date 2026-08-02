#WAP using function that add all odd numbers from 1 to n, n is given by the user
def add(n):
    sum=0
    for i in range(n+1):
        if(i%2!=0):
            sum+=i
    print(sum)           

n=int(input("Enter a number:"))
add(n) 