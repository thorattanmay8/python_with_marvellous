# 1
# Write a program which contains one lambda function which accepts one parameter and return power of two.
fun= int(input("Enter number : "))
data = lambda x: 2**x
output=data(fun)
print("Ans is : ",output)

# 2 
# Write a program which contains one lambda function which acccepts two parameters and return its multiplication. 
No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))
mult = lambda No1,No2: No1*No2
output=mult(No1,No2)
print("Multiplication is : ",output)

# 3 
# Write a program which contain filter(), map(), and reduce() in it. Python application which contains one list of 
# numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which 
# greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce 
# will return product of that numbers. 
from functools import reduce
data = []
size = int(input("Enter size of elements : "))
print("Enter list : ")
for i in range (size):
    a = int(input())
    data.append(a)
print("Input list : ",data)
fdata = list(filter(lambda x: 70<=x<=90 , data ))
print ("List after filter : ",fdata)
mdata = list(map(lambda x: x+10,fdata))
print ("List after map : ",mdata)
rdata = reduce(lambda x,y: x*y,mdata)
print ("Output of reduce : ",rdata)

# 4
# Write a program which contain filter(), map(), and reduce() in it. Python application which contains one list of 
# numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which 
# are even. Map function will calculate its square. Reduce will return addition of all that numbers. 
from functools import reduce
data = []
size = int(input("Enter size of elements : "))
print("Enter list : ")
for i in range (size):
    a = int(input())
    data.append(a)
print("Input list : ",data)
fdata = list(filter(lambda x: x%2==0 , data ))
print ("List after filter : ",fdata)
mdata = list(map(lambda x: x**2,fdata))
print ("List after map : ",mdata)
rdata = reduce(lambda x,y: x+y,mdata)
print ("Output of reduce : ",rdata)

# 5
# Write a program which contain filter(), map(), and reduce() in it. Python application which contains one list of 
# numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. Reduce will return maximum number of  that numbers.
from functools import reduce
data = []
size = int(input("Enter size of elements: "))
print("Enter list:")
for i in range(size):
    a = int(input())
    data.append(a)
print("Input list:", data)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
fdata = list(filter(is_prime, data))
print("List after filter:", fdata)
mdata = list(map(lambda x: x * 2, fdata))
print("List after map:", mdata)
rdata = reduce(lambda x, y: x if x > y else y, mdata)
print("Output of reduce:", rdata)
