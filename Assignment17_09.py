#Write a program which accept number from user and return number  of digits in that number. 
def digit(n):
    count = 0
    while n != 0:
        count += 1
        n = n//10
    return count
output = digit(int(input("Enter number : ")))
print("Digits in given number is : ",output)