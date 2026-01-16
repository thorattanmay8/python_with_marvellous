# 1 
# Write a program which contain one function named as Display() theat prints "Jay Ganesh" on console. 
def Display():
    print("Jay Ganesh")
Display()

# 2 
# Write a program which contains one function ChkGreater() that accepts two numbers and print the greater number. 
def ChkGreater():
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    if a > b:
        print(a, "is greater.")
    else:
        print(b, "is greater.")
ChkGreater()

# 3 
# Write a program which accepts one number and prints square of that number. 
a = int(input("Enter number : "))
print ("Square is : ",a**2)

# 4 
# Write a program which accepts one number and prints cube of that number. 
a = int(input("Enter number : "))
print ("Cube is : ",a**3)

# 5 
# Write a program which accepts one number and checks whether it is divisible by 3 and 5 
a = int(input("Enter number : "))
def divisible():
    if (a%3==0 and a%5==0):
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")
divisible()