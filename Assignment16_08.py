# 8 
# Write a program which accept number from user and print that number of "*" on screen. 
def star(n):
    for i in range(n):
        print("*",end = " ")
    print()
star(int(input("Enter number : ")))