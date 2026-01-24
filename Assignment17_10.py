#Write a program which accept number from user and return addition of digits in that number. 
def digit(n):
    sum = 0
    while n != 0:
        sum += n%10
        n=n//10
    return sum
output = digit(int(input("Enter number : ")))
print("Digits in given number is : ",output)