# 1
# Design a Python application that creates two threads named Prime and NonPrime. 
# - Both threads should accept a list of integers. 
# - The Prime thread should display all prime numbers from the list. 
# - The NonPrime thread should display all non-prime numbers from the list. 
import threading
Size = int(input("Enter size of elements : "))
print("Enter elements : ")
def PrimeList(data):
    p = []
    for n in data:
        count = 0

        for i in range(1,n+1):
            if (n%i==0):
                count += 1

        if count == 2:
            p.append(n)
    print("Prime numbers : ",p)

def NotPrimeList(data):
    NPNum = 0
    NP=[]
    for n in data:
        count = 0

        for i in range(1,n+1):
            if (n%i==0):
                count += 1
        
        if count!=2:
            NP.append(n)
    print("Non prime numbers : ",NP)

def main():
    data = []
    for i in range(Size):
        n = int(input())
        data.append(n)
    print(data)

    PrimeT = threading.Thread(target=PrimeList,args=(data,))
    NotPrimeT = threading.Thread(target=NotPrimeList,args=(data,))

    PrimeT.start()
    NotPrimeT.start()

    PrimeT.join()
    NotPrimeT.join()

if __name__ == "__main__":
    main()





# 2
# Design a Python application that creates two threads. 
# - Thread 1 should calculate and display the maximum element from an list. 
# - Thread 2 should calculate and display the minimum element from the same list. 
# - The list shoulf be accepted from the user.
import threading
Size = int(input("Enter size of elements : "))
print("Enter elements : ")
def maximum(data):
    M = data[0]
    for n in data:
        if n > M:
            M = n
    print("Maximum Number : ",M)


def minimum(data):
    Mi = data[0]
    for n in data:
        if n < Mi:
            Mi=n
    print("Minimum Number : ",Mi)
    

def main():
    data = []
    for i in range(Size):
        n = int(input())
        data.append(n)
    print(data)

    MaxT = threading.Thread(target=maximum,args=(data,))
    MinT = threading.Thread(target=minimum,args=(data,))

    MaxT.start()
    MinT.start()

    MaxT.join()
    MinT.join()

if __name__ == "__main__":
    main()




# Design a python application where multiple threads update a shared variable. 
# - Use a Lock to avoid race conditions. 
# - Each thread should increment the shared counter multiple times. 
# - Display the final value of the counter after all threads complete execution. 
import threading
count = [0]
lock = threading.Lock()
def thre(n,count,lock):
    for i in range(n):
        lock.acquire()
        count[0] += 1
        lock.release()


def main(n):
    thread1 = threading.Thread(target=thre,args=(n,count,lock))
    thread2 = threading.Thread(target=thre,args=(n,count,lock))
    thread3 = threading.Thread(target=thre,args=(n,count,lock))
    thread4 = threading.Thread(target=thre,args=(n,count,lock))
    thread5 = threading.Thread(target=thre,args=(n,count,lock))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    print("Final counter value : ",count[0])

if __name__=="__main__":
    main(int(input("Enter number : ")))




# Design a Python application that creates two threads. 
# - Thread 1 should compute the sum of elements from a list. 
# - Thread 2 should compute the product of elements from the same list. 
# - Return the results to the main thread and display them. 
import threading
from functools import reduce
Size = int(input("Enter size of elements : "))
print("Enter elements : ")
def add(data):
    sum = 0
    for n in data:
        sum += n
    print("Sum of elements : ",sum)

def product(data):
    value = reduce(lambda x,y: x*y ,data)
    print("Product of element is : ",value)

def main():
    data = []
    for i in range(Size):
        n = int(input())
        data.append(n)
    print(data)

    Sum_Thread = threading.Thread(target=add,args=(data,))
    Product_Thread = threading.Thread(target=product,args=(data,))

    Sum_Thread.start()
    Product_Thread.start()

    Sum_Thread.join()
    Product_Thread.join()

if __name__ == "__main__":
    main()

