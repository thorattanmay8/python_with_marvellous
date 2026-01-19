# 1 
# Write a program which accepts one number and check whether it is prime or not. 
n = int(input("Enter number : "))

def CheckPrime():
    for i in range (2,n):
        if (n%i==0):
            print(n,"is not prime number")
            return
    print("is prime number")
CheckPrime()

# 2
# Write a program which accepts one number and prints count of that digit in that number. 
no = int(input("Enter number : "))
count = 0 
def CountDigit():
    global count,no
    while no != 0:
        count = count + 1
        no = no // 10
    return
CountDigit()
print("Count is",count)

# 3
# Write a program which accepts one number and sum of digits. 
n = int(input("Enter number"))
sum = 0
def sumdigit():
    global n,sum
    while n != 0:
        sum = sum + (n%10)
        n = n // 10
    return
sumdigit()
print("Sum of digit is : ",sum)

# 4 
# Write a program which accepts one number and prints reverse. 
def reverse(n):
    ans = 0
    while n != 0:
        no1 = n % 10
        n = n // 10
        ans = ans * 10 + no1
    return (ans)
result = reverse(int(input("Enter number : ")))
print("Reverse output is : ",result)

# 5
# Write a program which accepts one number and checks whether it is palindrome or not. 
def palindrome(n):
    ans = 0 
    original = n
    while n!=0:
        no1 = n % 10 #321 - 1
        n = n // 10 #321 - 32
        ans = ans * 10 + no1 #1-2-3
    if ans == original:
        print(ans,"is palindrome")
    else:
        print(ans,"is not palindrome")
palindrome(int(input("Enter number : ")))

