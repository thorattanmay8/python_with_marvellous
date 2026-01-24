# Write a program which accepts one number and display below pattern. 
def pattern(n):
    for i in range(n):
        for j in range (n):
            print("*",end=" ")
        print()
pattern(int(input("Enter size : ")))