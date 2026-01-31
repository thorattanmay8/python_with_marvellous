# 1
# Write a Python program to implement a class named BookStore with the following specifications:
# - The class should contain two instance variables. 
#       - Name(Book Name)
#       - Author(Book Author)
# - The class should contain one class variable. 
#       - NoOfBooks (initialize it to 0) 
# - Define a constructor (__init__) that accepts Name and Author and initialize instance variables. 
# - Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created. 
# - Implement an instance method: 
#       - Display() - should display book details in the format:
#         <BookName> by <Author>. No of books: <NoOfBooks>

class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1 

    def Display(self,):
        print(self.Name,"by",self.Author,"No of books:",BookStore.NoOfBooks)

obj1 = BookStore("Linux system programming","Robert Love")
obj1.Display()

obj2 = BookStore("C programming","Dennis Ritchie")
obj2.Display()





# 2 
# Write a Python program to implement a class named BankAccount with the following requirements: 
# - The class should contain two instance variables:
#       - Name(Account holder name)
#       - Amount(Account balance)
# - The class should contain one variable:
#       - ROI (rate of. interest),initialized to 10.5
# - Define a constructor (__init__) that accepts Name and initial Amount. 
# - Implement the following instance methods:
#       - Display() - displays account holder name and current balance
#       - Deposite() - accept an amount from the user and adds it to balance 
#       - Withdraw() - accepts an amount from the user and subtracts it from the balance
#         (Ensure withdrawal is allowed only if sufficient balance exists)
#       - CalculateInterest() - calculates and returns interest using formula:
#         Interest = (Amount * ROI) / 100
# Create multiple objects and demonstrate all methods. 

class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account holder name : ",self.Name,"Current balance : ",self.Amount)

    def Deposite(self):
        dep = float(input("Enter amount to deposite : "))
        self.Amount = self.Amount + dep

    def Withdraw(self):
        wit = float(input("Enter amount to withdraw : "))
        if wit <= self.Amount:
            self.Amount = self.Amount - wit
        else:
            print ("Insufficient balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

obj1 = BankAccount("Tanmay",10000)
obj1.Display()
obj1.Deposite()
obj1.Withdraw()
print("Interest:", obj1.CalculateInterest())

obj2 = BankAccount("Shivam",11000)
obj2.Display()
obj1.Deposite()
obj1.Withdraw()
print("Interest:", obj2.CalculateInterest())




# 3
# Write a Python program to implement a class named Numbers with the following specifications:
# - The class should contain one instance variable:
#       - Value
# - Define a constructor(__init__) that accepts a number from the user and initialize Value. 
# - Implement the following instance methods:
#       - ChkPrime() - returns True if the number is prime, otherwise return False. 
#       - ChkPerfect() - return true if the number is perfect, otherwise return False. 
#       - Factors() - displays all factors of the number
#       - SumFactors() - returns the sum of all factors
#       (you may use this method as a helper in ChkPerfect() if required)
# - Create multiple objects and call all methods

class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors are:", end=" ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total = total + i
        return total

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False


obj1 = Numbers(28)
print("Is Prime:", obj1.ChkPrime())
print("Is Perfect:", obj1.ChkPerfect())
obj1.Factors()
print("Sum of factors:", obj1.SumFactors())

obj2 = Numbers(15)
print("Is Prime:", obj2.ChkPrime())
print("Is Perfect:", obj2.ChkPerfect())
obj2.Factors()
print("Sum of factors:", obj2.SumFactors())
