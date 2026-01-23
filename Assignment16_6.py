# 6
# Write a program which accept number from user and cheeck whether that number is positive or negative or zero. 
def CheckNum(n):
    if n>0:
        print("Positive number")
    elif n<0:
        print("Negative number")
    else:
        print("Zero")
CheckNum(int(input("Enter number : ")))