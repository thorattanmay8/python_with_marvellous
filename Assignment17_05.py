# Write a program which accept one number for user and check whether is prime or not. 
def CheckPrime(n):
    for i in range (2,n):
        if (n%i==0):
            print(n,"is not prime number")
            return
    print(n,"is prime number")
CheckPrime(int(input("Enter number : ")))
