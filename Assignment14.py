# 1
# Write a lambda function which accepts one number and returns square of that number. 
a = int(input("Enter number : "))
square = lambda a: a**2
ret = square(a)
print("Square is : ",ret)

# 2
# Write a lambda function which accepts one number and returns cube of that number. 
no = int(input("Enter number : "))
cube = lambda a: no**3
ret = cube(no)
print("Cube is : ",ret)

# 3
# Write a lambda function which accepts two number and returns maximum number.
no1 = int(input("Enter first number : "))
no2 = int(input("Enter second number : "))
greater = lambda no1,no2: no1 if no1>no2 else no2
ret = greater(no1,no2)
print("Maximum number is : ",ret)

# 4
# Write a lambda function which accepts two number and returns minimum number.
no1 = int(input("Enter first number : "))
no2 = int(input("Enter second number : "))
smaller = lambda no1,no2: no1 if no1<no2 else no2
got = smaller(no1,no2)
print("Minimum number is : ",got)

# 5
# Write a lambda function which acepts one number and return True if number is even otherwise false. 
no = int(input("Enter number : "))
CheckEven = lambda no: True if no%2==0 else False
got = CheckEven(no)
print("Number is even : ",got)

# 6
# Write a lambda function which acepts one number and return True if number is odd otherwise false. 
no = int(input("Enter number : "))
CheckOdd = lambda no: True if no%2!=0 else False
got = CheckOdd(no)
print("Number is even : ",got)

# 7
# Write a lambda function which accepts one number and returns True if divisible by 5. 
no = int(input("Enter number : "))
div = lambda no: True if no%5==0 else False
got = div(no)
print("Disible by 5 : ",got)

# 8 
# Write a lambda function which accepts two number and return addition. 
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
add = lambda a,b: a + b
ret = add(a,b)
print("Addition is : ",ret)

# 9
# Write a lambda function which accepts two numbers anad return multiplication. 
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
mult = lambda a,b: a * b
ret = mult(a,b)
print("Multiplication is : ",ret)

# 10 
# Write a lambda function which accept three numbers and return largest number. 
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
greater = lambda a,b,c: a if a > b and a > c  else (b if b > a and b > c else c)
got = greater(a,b,c)
print("Largest number is  : ",got)