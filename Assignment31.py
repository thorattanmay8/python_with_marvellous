# 1) Design automation script which accept directory name and file extension from user. Display all
# files with that extention
import sys
import os

def Extension(directory, Extension):
    Ret = os.path.exists(directory)
    if Ret == False:
        print("There is no such directory")
        return

    Ret = os.path.isdir(directory)
    if Ret == False:
        print("It is not a directory")
        return

    for FolderName, SubFolderName, FileName in os.walk(directory):
        for fname in FileName:
            if fname.endswith(Extension):
                print("File name : ",os.path.join(FolderName, fname))


def main():
    if (len(sys.argv)==1):
        print("Enter directory name")
        return
    Ext = input("Enter file estension : ")
    Extension(sys.argv[1],Ext)

if __name__=="__main__":
    main()



# 2) Design a automation script which accept directory name and two file extensions from user. 
# Rename all files with first file extension with the second file extension. 
import sys
import os

def Rename(DirName,Ext1,Ext2):
    Ret = False
    Ret = os.path.exists(DirName)
    if Ret == False:
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if Ret == False:
        print(f"{DirName} is not Directory")
        return

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            if fname.endswith(Ext1):
                old_path = os.path.join(FolderName,fname)

                new_name = fname.replace(Ext1,Ext2)
                new_path = os.path.join(FolderName, new_name)

                os.rename(old_path, new_path)
                print("Renamed : ",fname, "-",new_name)

def the():
    if (len(sys.argv)==1):
        print("Enter Directory Name : ")
        return
    
    Ext1 = input("Enter first file extension : ")
    Ext2 = input("Enter secont file extension : ")

    Rename(sys.argv[1],Ext1,Ext2)

def main():
    the()
if __name__ == "__main__":
    main()


# 3) Design automation script which accept two directory names. Copy all files from the first directory
# into second directory. Second directory should be created at run time. 
import sys
import os

def CopyFiles(Directory1,Directory2):
    Ret = os.path.exists(Directory1)
    if Ret == False:
        print("There is no such directory")
        return

    Ret = os.path.exists(Directory2)
    if Ret == False:
        os.mkdir(Directory2)
    
    Ret = os.path.isdir(Directory1)
    if Ret == False:
        print(f"{Directory1} it not directory.")
        return

    Ret = os.path.isdir(Directory2)
    if Ret == False:
        print(f"{Directory2} it not directory.")
        return

    for FolderName, SubFolderName, FileName in os.walk(Directory1):
        for fname in FileName:
            sourcepath = os.path.join(FolderName, fname)
            destpath = os.path.join(Directory2,fname)

            if os.path.isfile(sourcepath):
                fsource = open(sourcepath,"rb")
                fdest = open(destpath,"wb")

                data = fsource.read()
                fdest.write(data)

                fsource.close()
                fdest.close()

    print("Directory files copied successfully")
            
def main():
    if (len(sys.argv)<3):
        print("Enter two directory name")
        return
    CopyFiles(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()



# 4) Design automation script which accept two directory names and one file extension. Copy all files
# with the specified extension from first directory into second directory. Second directory should
# be created at run time. 

import sys
import os

def CopyFiles(Directory1,Directory2,Extension):
    Ret = os.path.exists(Directory1)
    if Ret == False:
        print("There is no such directory")
        return

    Ret = os.path.exists(Directory2)
    if Ret == False:
        os.mkdir(Directory2)
    
    Ret = os.path.isdir(Directory1)
    if Ret == False:
        print(f"{Directory1} it not directory.")
        return

    Ret = os.path.isdir(Directory2)
    if Ret == False:
        print(f"{Directory2} it not directory.")
        return

    for FolderName, SubFolderName, FileName in os.walk(Directory1):
        for fname in FileName:
            if fname.endswith(Extension):
                sourcepath = os.path.join(FolderName, fname)
                destpath = os.path.join(Directory2,fname)

                if os.path.isfile(sourcepath):
                    fsource = open(sourcepath,"rb")
                    fdest = open(destpath,"wb")

                    data = fsource.read()
                    fdest.write(data)

                    fsource.close()
                    fdest.close()

    print("Directory files copied successfully")
            
def main():
    if (len(sys.argv)<3):
        print("Enter two directory name")
        return
    Ext = input("Enter file extension : ")
    CopyFiles(sys.argv[1],sys.argv[2],Ext)

if __name__ == "__main__":
    main()
