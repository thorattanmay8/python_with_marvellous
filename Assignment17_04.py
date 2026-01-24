# Write a program which accepts one number from user and return addition of its factors. 
def factor(n):
    sum = 0
    for i in range (1,n+1):
        if n % i == 0:
            sum += i
    return sum
ans = factor(int(input("Enter number : ")))
print ("Addition of factors is : ",ans)