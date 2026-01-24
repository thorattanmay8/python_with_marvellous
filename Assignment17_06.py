#Write a program which accept one number and display below pattern. 
def pattern(n):
    for i in range(n,0,-1):
        for j in range (i):
            print("*",end=" ")
        print()
pattern(int(input("Enter size : ")))