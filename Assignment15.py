from functools import reduce
# 1
# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number. 
def main():
    data = []
    Size = (int(input('Enter number of elements : ')))
    print("Enter elements : ")
    for i in range (Size):
        value = int(input())
        data.append(value)
    FData = list(map(lambda data: data**2,data))
    print("Square of ",data,"are",FData)
main()

# 2
# Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers. 
def even():
    data = []
    size = (int(input("Enter size of data : ")))
    print("Enter numbers : ")
    for i in range (size):
        value = int(input())
        data.append(value)
    FData = list(filter(lambda data: data%2==0,data))
    print(data,"Even number are",FData)
even()

# 3
# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers. 
def odd():
    data = []
    size = (int(input("Enter size of data : ")))
    print("Enter numbers : ")
    for i in range (size):
        value = int(input())
        data.append(value)
    FData = list(filter(lambda data: data%2!=0,data))
    print(data,"Odd number are",FData)
odd()

# 4
# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements. 
def sum():
    data = []
    size = (int(input("Enter size of data : ")))
    print("Enter numbers : ")
    for i in range (size):
        value = int(input())
        data.append(value)
    FData = reduce(lambda x,y: x+y,data)
    print(data,"sum is",FData)
sum ()

# 5 
# Write a lambda function using reduce() which accepts multiple numbers and returns the maximum elements. 
def max():
    data = []
    size = (int(input("Enter size of data : ")))
    print("Enter numbers : ")
    for i in range (size):
        value = int(input())
        data.append(value)
    FData = reduce(lambda x,y: x if x > y else y,data)
    print(data,"maximum is",FData)
max ()

# 6
# Write a lambda function using reduce() which accepts multiple numbers and returns the minimum elements. 
def min():
    data = []
    size = (int(input("Enter size of data : ")))
    print("Enter numbers : ")
    for i in range (size):
        value = int(input())
        data.append(value)
    FData = reduce(lambda x,y:x if x<y else y,data)
    print(data,"minmum is",FData)
min()

# 7 
# Write a lambda function using filter() which accept list  of string and returns a list of strings having length greater than 5. 
def string_lenngth(x):
    count = 0
    for x in x:         # count each character from the string 
        count +=1       # count = count+1
    return count
def main():
    data=[]
    size = int(input("Enter size of elements : "))
    print("Enter element : ")
    for i in range (size):
        data.append(input())
    final = list(filter(lambda x: string_lenngth(x) > 5, data))
    print ("Strings having length greater than 5 : ", final)
main()

# 8
# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5. 
def div ():
    data = []
    n = int(input("Enter size of elements : "))
    print ("Enter elements : ")
    for i in range(n):
        data.append(int(input()))
    value = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, data))
    print("Output is : ",value)
div()

# 9
# Write a lambda function using reduce() which accepts a list of numbers and return the product of all elements. 
def product():
    data = []
    n = int(input("Enter size of element : "))
    print("Enter elements : ")
    for i in range(n):
        data.append(int(input()))
    value = reduce(lambda x,y: x*y ,data)
    print("Product of element is : ",value)
product()

# 10
# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers. 
def CountEven():
    data=[]
    n = int(input("Enter list of elements : "))
    print("Enter elements : ")
    for i in range(n):
        data.append(int(input()))
    value = list(filter(lambda x: x%2==0,data))
    count = 0 
    for i in value:
        count += 1 
    print("Output is : ",count)
CountEven()