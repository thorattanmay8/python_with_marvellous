# 1
# Write a program which accepts one number and prints multiplication table of that number.
n = int(input("Enter number : "))
for i in range (1,11,1):
    print(n*i)

# 2
# Write a program which accepts one number and prints sum of first n natural numbers.
n = int(input("Enter number : "))
for i in range (1,n+1,1):
    print(i)
Sum = 0
for i in range(1,n+1,1):
    Sum = Sum + i
print("Summation is", Sum)

# 3
# Write a program which accept one number and print factorial of that number.
n = int(input("Enter number : "))
Factorial = 1
for i in range(1,n+1,1):
    Factorial = Factorial * i
print("Factorial is : ",Factorial)

# 4
# Write a program which accepts one number and prints all even numbers till that number.
n = int (input("Enter number : "))
for i in range (1,n+1):
    if (i%2==0):
        print(i)
    else:
        print

# 5
# Write a program which accepts one number and prints all odd numbers till that number.
n = int (input("Enter number : "))
for i in range (1,n+1):
    if (i%2!=0):
        print(i)
    else:
        print
