# # 1) Count Lines in a File
# # Problem Statement:
# # Write a program which accepts a file name from the user and counts how many lines are present in the file. 
import sys
import os

def LineCount(FileName):
    Count = 0
    if os.path.exists(FileName):
        fobj = open(FileName,"r")
        for line in fobj:
            Count += 1
        print("Number of line : ",Count)
        fobj.close()
        
    else:
        print("File not exist")

def main():
    if (len(sys.argv)==1):
        print("Enter file name")
        return
    LineCount(sys.argv[1])

if __name__ == "__main__":
    main()


# 2) Count Words in a File
# Write a program which accepts a file name from the user and counts the total number of words in that file. 
import sys
import os

def WordCount(FileName):
    Count = 0
    if os.path.exists(FileName):
        fobj = open(FileName,"r")
        for line in fobj:
            temp =""
            for ch in line:
                if ch!=" " and ch!="\n" and ch!= "\t":
                    temp += ch
                
                else:
                    if temp != "":
                        Count += 1
                        temp = ""
            if temp != "":
                Count += 1
        print("Number of words in file : ",Count)
        fobj.close()
        
    else:
        print("File not exist")

def main():
    if (len(sys.argv)==1):
        print("Enter file name")
        return
    WordCount(sys.argv[1])

if __name__ == "__main__":
    main()

# 3) Display File Line by Line
# Problem Statement:
# Write a program which accepts a file name from the user and dislays the contents of the file line by line on the screen. 
import sys
import os
import time 

def Content(FileName):
    if os.path.exists(FileName):
        fobj = open(FileName,"r")
        print("Contents of the file is: \n")
        for data in fobj:
            print(data)
            time.sleep(0.05)
        fobj.close()
    else:
        print("There is no such file")

def main():
    if (len(sys.argv)==1):
        print("Enter file name")
        return
    Content(sys.argv[1])
        
if __name__=="__main__":
    main()



# 4) Copy File Contents into Another File.
# Problem Statement:
# Write a program which accepts two file names from the user. 
#   -First file is an existing file
#   -Second file is a new file 
# Copy all contents form the first file into the second file. 

import os
import sys

def CopyData(FileName1,FileName2):
    if os.path.exists(FileName1):
        fobj = open(FileName1,"r")
        data = fobj.read()
        
        dobj = open(FileName2,"w")
        dobj.write(data)

        fobj.close()
        dobj.close()

        print(f"Contents of {FileName1} copied into {FileName2}")
    else :
        print("File not exists")
def main():
    if (len(sys.argv)!=3):
        print("Please enter two filename")
        return
    
    CopyData(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()



# 5) Search a Word in File 
# Problem Statement: 
# Write a program which accepts a file name and a word from the user and checks wherther 
# that word is present in the file or not. 
import sys
import os

def word(FileName):
    inp = (input("Enter word : "))

    if os.path.exists(FileName):
        fobj = open(FileName)
        data = fobj.read()

        if inp in data:
            print(f"{inp} is present in {FileName}")
        else:
            print(f"{inp} is not present in {FileName}")
        fobj.close()

def main():
    if (len(sys.argv) == 1):
        print("Enter file name please")
        return
    word(sys.argv[1])

if __name__ == "__main__":
    main()