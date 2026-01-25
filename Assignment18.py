# 1 
# Write a program which accept N numbers from user and store it into List. Return addition of all elements from that list. 
def AddList():
    sum = 0
    data=[]
    n = int(input("Enter list of elements : "))
    print("Enter elements : ")
    for i in range(n):
        data.append(int(input()))
        sum = sum + data[i]
    print("Addition of all numbers is : ",sum)
AddList()

# 2 
# Write a program which accept N numbers from user and store it into List. Return Maximum number from that list. 
def maximum():
    data=[]
    n = int(input("Enter list of elements : "))
    print("Enter elements : ")
    maxi = int(input())
    for i in range(n-1):
        num = (int(input()))
        if num > maxi:
            maxi = num
    print("Maximum numbers from list is : ",maxi)
maximum()

# 3
# Write a program which accept N number from user and store it into List. Return Minimum number from that list
def minimum():
    data=[]
    n = int(input("Enter list of elements : "))
    print("Enter elements : ")
    mini = int(input())
    for i in range(n-1):
        num = (int(input()))
        if num < mini:
            mini = num
    print("Minimum numbers from list is : ",mini)
minimum()

# 4
# Write a program which accepts N number from user and store it into List. Accept one another number from user and return frequency of that number from list. 
def frequency():
    data = []
    n = int(input("Enter number of elements: "))
    print("Enter elements:")
    for i in range(n):
        data.append(int(input()))
    x = int(input("Enter number to find frequency: "))
    count = 0
    for num in data:
        if num == x:
            count += 1
    print(f"Frequency of input is: ",count)
frequency()

# 5 
# Write a program which accept N numbers from user and store it into list. Return addition of all 
# prime numbers from that list. Main python file accepts N numbers from user and pass each 
# number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name
# of the function from main python file should be ListPrime

import MarvellousNum_18_Module

def ListPrime():
    data = []
    n = int(input("Enter number of elements: "))
    print("Enter elements:")
    for i in range(n):
        data.append(int(input()))
    sum_primes = 0
    for num in data:
        if MarvellousNum_18_Module.ChkPrime(num):
            sum_primes += num
    print("Addition of all prime numbers is:", sum_primes)
ListPrime()