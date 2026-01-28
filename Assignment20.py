# 1 
# Design a Python application that creates two separate thread named Even and Odd. 
# - The Even thread should display the first 10 even numbers. 
# - The Odd thread should display the first 10 odd numbers. 
# - Both threads should execute independently using the threading module. 
# - Ensure proper thread creation and execution. 
import threading

def Even():
    print("First 10 even numbers : ")
    for i in range (2,21,2):
        print(i,end=", ")
    print()

def Odd():
    print("\nFirst 10 odd numbers : ")
    for i in range (1,21,2):
        print(i,end=", ")
    print()

def main():
    EvenT = threading.Thread(target=Even)
    OddT = threading.Thread(target=Odd)

    EvenT.start()
    OddT.start()

    EvenT.join()
    OddT.join()

if __name__ == "__main__":
    main()



# 2 
# Design a Python application that creates two threads named EvenFactor and OddFactor. 
# - Both threads should accept one integer number as a parameter.
# - The EvenFactor thread should:
#   - Identify all even factors of the given number. 
#   - Calculate and display the sum of even factors. 
# - The Odd ThreadFactor thread should:
#   - Identify all odd factors of the given number. 
#   - Calculate and display the sum of odd factors. 
# - After both threads complete execution, the main thread should display the message:
# "Exit from main"
import threading

def EvenFactor(No):
    sum = 0
    print("Even factors are : ")
    for i in range(1,No+1):
        if No%i==0 and i%2 ==0:
            print(i,end=", ")
            sum += i
    print("Sum of Even factors is : ",sum)

def OddFactor(No):
    sum = 0
    print("Odd factors are : ")
    for i in range(1,No+1):
        if No%i==0 and i%2!=0:
            print(i,end=", ")
            sum += i
    print("\nSum of Odd factors is : ",sum)

def main():
    No = int(input("Enter parameter : "))

    EvenT = threading.Thread(target=EvenFactor,args=(No,))
    OddT = threading.Thread(target=OddFactor,args=(No,))

    EvenT.start()
    OddT.start()

    EvenT.join()
    OddT.join()

    print("Exit from main")

if __name__ == "__main__":
    main()



# 3
# Design a Python application that creates two threads named EvenList and OddList. 
# - Both threads should accept a list of integers as input. 
# - The EvenList thread should :
#   - Extract all even elements from the list. 
#   - Calculate and display their sum. 
# - The OddList thread should : 
#   - Extract all odd elements from the list. 
#   - Calculate and display their sum. 
# Threads should run concurrently. 
import threading

Size = int(input("Enter size of elements : "))
print("Enter elements : ")
def EvenList(data):
    EvenNum=0
    EveN=[]
    for elements in data:
        if elements%2==0:
            EvenNum += elements
            EveN.append(elements)
    print("List of even numbers is : ",EveN)
    print("Sum of even numbers  : ",EvenNum)

def OddList(data):
    OddNum = 0
    OddN=[]
    for elements in data:
        if elements%2!=0:
            OddNum += elements
            OddN.append(elements)
    print("List of odd numbers is : ",OddN)
    print("sum of odd numbers : ",OddNum)

def main():
    data = []
    for i in range(Size):
        n = int(input())
        data.append(n)
    print(data)

    EvenListT = threading.Thread(target=EvenList,args=(data,))
    OddListT = threading.Thread(target=OddList,args=(data,))

    EvenListT.start()
    OddListT.start()

    EvenListT.join()
    OddListT.join()

if __name__ == "__main__":
    main()


# 4
# Design a Python application that creates three threads named Small, Capital, and Digits. 
# - All threads should accepts a string as input. 
# - The small thread should count and display the number of lowercase characters. 
# - The capital thread should count and display the number of uppercase characters. 
# - The Digits thread should count and display the number of numeric digits. 
# - Each thread must also diplay: 
#       - Thread ID
#       - Thread Name
import threading

def Small(s):
    lower=0
    for ch in s:
        if ch.islower():
            lower+=1
    print("Count of Lowecase letters : ",lower)
    print("Thread ID : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)

def Capital(s):
    upper=0
    for ch in s:
        if ch.isupper():
            upper+=1
    print("Count of Uppercase letters : ",upper)
    print("Thread ID : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)

def Digit(s):
    digit=0
    for ch in s:
        if ch.isdigit():
            digit+=1
    print("Count of Digits : ",digit)
    print("Thread ID : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)

def main():
    s = str(input("Enter name : "))
    
    SmallT = threading.Thread(target=Small,args=(s,))
    CapitalT=threading.Thread(target=Capital,args=(s,))
    DigitT= threading.Thread(target=Digit,args=(s,))

    SmallT.start()
    CapitalT.start()
    DigitT.start()

    SmallT.join()
    CapitalT.join()
    DigitT.join()

if __name__ == "__main__":
    main()


# 5
# Design a Python application that creates two threads named Thread1 and Thread2.
# - Thread1 should display numbers from 1 to 50.
# - Thread2 should display number from 50 to 1 in reverse order. 
# Ensure that : 
#   - Thread2 starts execution only after Thread1 has completed. 
# Use appropriate thread synchronization. 
import threading

def forward():
    for i in range(1,51):
        print(i,end=" ")
    print()

def backward():
    for i in range(50,0,-1):
        print(i,end=" ")
    print()

def main():

    Thread1 = threading.Thread(target=forward)
    Thread2 = threading.Thread(target=backward)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

if __name__=="__main__":
    main()