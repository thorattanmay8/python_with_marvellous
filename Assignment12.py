# 1 
# Write a program which accepts one character and checks whether it is vowel or consonant. 
char = str(input("Enter character : "))

def checkchar():
    if char == "a":
        print(char,"is vowel")
    elif char == "e":
        print(char,"is vowel")
    elif char == "i":
        print(char,"is vowel")
    elif char == "o":
        print(char,"is vowel")
    elif char == "a":
        print(char,"is vowel")
    else:
        print(char,"is consonant")
checkchar()

# 2
# Write a program which accepts one number and prints its factors. 
def factor(n):
    for i in range (1,n+1):
        if n % i == 0:
            print ("Output is : ",i)
factor(int(input("Enter number : ")))

#3
# Write a program which accepts one number and prints addition, subtraction, multiplication and division. 
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

def Calculator():
    global a,b
    print("Addition : ",a+b)
    print("Subtraction : ",a-b)
    print("Multiplication : ",a*b)
    print("Division : ",a/b)
Calculator()

# 4
# Write a program which accepts one number and prints that many numbers starting from 1. 
def number(n):
    print("Output is : ",end = " ")
    for i in range (1,n+1):
        print(i, end = " ")
    print() 
number(int(input("Enter number : ")))

# 5 
# Write a program which accepts one number and print that many numbers in reverse order. 
def rev(n):
    print ("Output is ",end =" ")
    for i in range(n,0,-1):
        print (i,end=" ")
    print()

rev(int(input("Enter number : ")))