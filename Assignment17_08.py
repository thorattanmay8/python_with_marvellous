#Write a program which accept one number and display below pattern. 
def pattern(n):
    for i in range(1,n+1):
        for j in range (1,i+1):
            print(j,end=" ")
        print()
pattern(int(input("Enter size : ")))