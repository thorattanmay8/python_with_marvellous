# 1 
# Write a program which accepts length and width of rectangle and prints area. 
def Rarea(length,width):
    area = length * width
    return area
area = Rarea(
    float(input("Enter lenght of rectangle : ")),
    float(input("Enter width of rectangle : "))
)
print("Area of rectangle is : ",area)

# 2 
# Write a pogram which accepts radius of circle and prints area of circle. 
def carea(r):
    cutiepie = 3.14
    area = cutiepie * (r**2)
    return area
area = carea(float(input("Enter radius of circle : ")))
print("Area of circle is : ",area)

# 3
# Write a program which accepts one number and check whether it is perfect number or not. 
def perfect(n):
    sum = 0
    for i in range (1,n):
        if n%i==0:
            sum = sum + i
    if sum == n:
        print(n,"is perfect number")
    else:
        print(n,"is not perfect number")

perfect(int(input("Enter one number : ")))

# 4 
# Write a program which accepts one number and prints binary equivalent. 
def binary(n):
    store = 0 
    while n != 0 :
        remainder = n%2
        store =  store * 10 + remainder
        n = n//2 
    reversed_num = 0
    while store != 0:
        digit = store % 10
        reversed_num = reversed_num * 10 + digit
        store = store // 10
    print("output : ",reversed_num)
binary(int(input('Enter one number : ')))    

# 5
# Write a program accepts marks and display grade. 
n = int (input("Enter marks : "))
if n >= 75:
    print("Distinction")
elif n>= 60:
    print("First class")
elif n>=50:
    print("Second class")
else:
    print("Fail")