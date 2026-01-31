# 1 
# Write a Python program to implement a class named Demo with the following specification:
# The class should contain one class variable named Value. 
# Define a constructor(__init__)that acccept two parameters and initialize the instance variables. 
# Implement two instance methods : 
#       - Fun() - displays the value of instance variables no1 and no2. 
#       - Gun() - displays the value of instance variables no1 and no2. 
# Create two object of the demo class as follows : 
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)
# Call the instance methods in the given sequence : 
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

class Demo:
    Value = 0
    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def Fun(self):
        print(self.no1,self.no2)

    def Gun(self):
        print(self.no1,self.no2)


obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()

# 2
# Write a Python progrma to implement a class named Circle with the following requirements:
# - The class should contain three instance variables: Radius,Area, and Circumference.
# - The class should contain one class variable named PI,initialized to 3.14. 
# - Define a constructor (__init__) that initialize all instance variable to 0.0. 
# - Implement the following instance methods:
#       -Accept() - accept the radius of the circle from the user. 
#       -CalculateArea() - calculates the area of the circle and stores it in the Area variable. 
#       - CalculateCircumference() - calculate the Circumference of the circle and stores it in the Circumference variable. 
#       - Display() - display the value of Radius,Area,and Circumference. 
# - Create multiple objects of the circle class and invoke all the instance methods for each object. 

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        self.Radius = float(input("Enter radius of circle : "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def display(self):
        print("Radiuse of circle is : ",self.Radius)
        print("Area of circle is : ",self.Area)
        print("Circumference of circle is : ",self.Circumference)

obj1 = Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.display()

obj2 = Circle()
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.display()

obj3 = Circle()
obj3.Accept()
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.display()

# 3
# Write a Python program to implement a class named Arithmetic with the following characteristic: 
# - The class should contain two instance variablel: Value1 and Value2. 
# - Define a constructor(__init__) that initialize all instance variable to 0. 
# - Implement the following instance methods: 
#       - Accept() - accepts values for Value1 and Value2 from the user. 
#       - Addition() - return the addition of Value1 and Value2.
#       - Subtraction() - returns the subtraction of Value1 and Value2.
#       - Multiplication() - return the multiplication of Value1 and Value2. 
#       - Division() - return the division of Value1 and Value2 (handle division by zero properly)
# - Create multiple object of the Arithmetic class and invoke all the instance methods. 

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number : "))
        self.Value2 = int(input("Enter second number : "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero not allowed"
        return self.Value1 / self.Value2

obj1 = Arithmetic()
obj1.Accept()
print("Addition is : ",obj1.Addition())
print("Subtraction is : ",obj1.Subtraction())
print("Multiplication is : ",obj1.Multiplication())
print("Division is : ",obj1.Division())

obj2 = Arithmetic()
obj2.Accept()
print("Addition is : ",obj2.Addition())
print("Subtraction is : ",obj2.Subtraction())
print("Multiplication is : ",obj2.Multiplication())
print("Division is : ",obj2.Division())

obj3 = Arithmetic()
obj3.Accept()
print("Addition is : ",obj3.Addition())
print("Subtraction is : ",obj3.Subtraction())
print("Multiplication is : ",obj3.Multiplication())
print("Division is : ",obj3.Division())