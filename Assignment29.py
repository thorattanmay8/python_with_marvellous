# 1 
# Check File Exists in current Directory 
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in 
# the current directory or not. 

import os 
def main():
    FileName = input("Enter file name : ")

    Ret = os.path.exists(FileName)

    if (Ret==True):
        print("File exists in current directory.")

    else:
        print("File not exists in current directory.")

if __name__=="__main__":
    main()

# 2
# Display file contents 
# Problem statement:
# Write a program which accepts a file name from the user, opens that file and displays the entire
# contents on the console. 

import os 
def main():
    FileName = input("Enter file name : ")

    if os.path.exists(FileName):

        fobj = open(FileName,"r")

        Data = fobj.read()

        print("Content from file : ",Data)

        fobj.close()

    else:
        print("File not exists in current directory.")

if __name__=="__main__":
    main()



# 3
# Copy file contents into a new file (command line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a 
# new file named Demo.txt, and copies all contents from the given file into Demo.txt. 

import os
import sys

def CopyData(FileName):
    if os.path.exists(FileName):
        fobj = open(FileName,"r")
        data = fobj.read()
        
        dobj = open("Demo.txt","w")
        dobj.write(data)

        fobj.close()
        dobj.close()

    print("File copied successfully.")

def main():
    if (len(sys.argv)!=2):
        print("Please enter filename first")
        return
    
    CopyData(sys.argv[1])

if __name__ == "__main__":
    main()




# 4
# Compare Two Files (command line)
# Problem Statement:
# Write a program which accepts two file name through command line arguments and compares the contents 
# of both files. 
# - If both files contains the same contents, display Success
# - Otherwise display Failure
import sys
import os

def CompareFiles(FileName1,FileName2):
    if os.path.exists(FileName1):
        if os.path.exists(FileName2):
            Obj1 = open(FileName1,"r")
            Obj2 = open(FileName2,"r")

            data1 = Obj1.read()
            data2 = Obj2.read()

            Obj1.close()
            Obj2.close()

            if data1 == data2:
                print("Success")
            else:
                print("Failure")
        else:
            print("File not exist")
def main():
        if (len(sys.argv)!= 3):
            print("Please give two file names.")
            return
        CompareFiles(sys.argv[1],sys.argv[2])
if __name__ == "__main__":
    main()

# 5
# Frequency of a string in file. 
# Problem statement :
# Write a program which accepts a file name and one string from the user and returns 
# frequency (count of occurrences) of that string in the file. 
import sys 
import os

def File(FileName):
    occurrences = 0
    A = str(input("Enter string name : "))

    if os.path.exists(FileName):
        oobj = open(FileName,"r")
        data = oobj.read()
        occurrences = data.count(A)
        print("Frequency of string is : ",occurrences)
        oobj.close()

    else : 
        print("File not exist")

def main():
    if (len(sys.argv) == 1):
        print("Please enter file name ")
        return
    
    File(sys.argv[1])
if __name__ == "__main__":
    main()