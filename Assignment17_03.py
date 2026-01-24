# Write a program which accept one number from user and return it factorial. 
def fact(n):
    Value = 1
    for i in range(1,n+1):
        Value = Value * i
    return Value
output=fact(int(input("Enter number : ")))
print("Factorial is : ",output)