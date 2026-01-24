# Create on module named as Arithmetic which contain 4 function as Add() for addition,
#  Sub() for subtraction,mult() for multiplication and Div() for division. 
# All function accepts two parameters as number and perform the operation. 
# Write on python program which call all the functions from arithmetic module 
# by accepting the parameters from user. 
import Assignment17_01Module

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

Result = Assignment17_01Module.Add(a,b)
print('Addition is : ',Result)

Result = Assignment17_01Module.Sub(a,b)
print('Substraction is : ',Result)

Result = Assignment17_01Module.Mult(a,b)
print('Multiplication is : ',Result)

Result = Assignment17_01Module.Div(a,b)
print('Division is : ',Result)