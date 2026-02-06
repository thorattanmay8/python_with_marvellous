# # 1) Design automation script which accept directory name and display checksum of all files. 
# import os
# import sys
# import hashlib

# def checksum(Directory):
#     Ret = os.path.exists(Directory)
#     if Ret == False:
#         print("There is no such directory")
#         return

#     Ret = os.path.isdir(Directory)
#     if Ret == False:
#         print(f"{Directory} is not directory")
#         return

#     for FoldeName, SubFolderName, FileName in os.walk(Directory):
#         for fname in FileName:
#             filepath = os.path.join(FoldeName, fname)

#             if os.path.isfile(filepath):
#                 fobj = open(filepath, "rb")
#                 data = fobj.read()
#                 fobj.close()

#                 hashobj = hashlib.md5(data)
#                 print(fname,"Checksum : ", hashobj.hexdigest())
# def main():
#     if (len(sys.argv)==1):
#         print("Enter directory name")
#         return
#     checksum(sys.argv[1])

# if __name__ == "__main__":
#     main()




# # 2) Design automation script which accept directory name and write names of duplicate files from 
# # that directory into log file named as Log.txt. Log.txt file should be created into current directory
# import sys
# import os

# def LogDirectory(DirectoryName):
#     if os.path.exists(DirectoryName) == False:
#         print("There is no such directory")
#         return
    
#     if os.path.isdir(DirectoryName) == False:
#         print(f"{DirectoryName} is not a directory")
#         return

#     FileDict = {}

#     for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
#         for fname in FileName:
#             if fname in FileDict:
#                 FileDict[fname] +=1
#             else:
#                 FileDict[fname] = 1

#     fobj = open("Log.txt","w")

#     for fname in FileDict:
#         if FileDict[fname]>1:
#             fobj.write(fname+"\n")
#     fobj.close()
#     print("Duplicate file names written in log.txt file")

# def main():
#     if (len(sys.argv)==1):
#         print("Enter directory name")
#         return
#     LogDirectory(sys.argv[1])

# if __name__ == "__main__":
#     main()

# # 3) Design automation script which accepts directory name and delete all duplicate files from that 
# # directory. Write names of duplicate files from that directory into log file named as Log.txt. 
# # Log.txt file should be created into current directory

# import sys
# import os
# import hashlib

# def DirectoryScanner(DirName):

#     if not os.path.exists(DirName):
#         print("There is no such directory")
#         return

#     if not os.path.isdir(DirName):
#         print("It is not a directory")
#         return

#     fobj = open("Log.txt", "w")

#     FileDict = {}
#     TotalFiles = 0
#     DuplicateCount = 0

#     for FolderName, SubFolder, FileNames in os.walk(DirName):
#         for fname in FileNames:
#             TotalFiles += 1
#             FilePath = os.path.join(FolderName, fname)

#             hobj = hashlib.md5()
#             f = open(FilePath, "rb")
#             hobj.update(f.read())
#             f.close()

#             FileHash = hobj.hexdigest()

#             if FileHash in FileDict:
#                 fobj.write("Duplicate file deleted : " + FilePath + "\n")
#                 os.remove(FilePath)
#                 DuplicateCount += 1
#             else:
#                 FileDict[FileHash] = FilePath

#     fobj.write("\nTotal files scanned : " + str(TotalFiles) + "\n")
#     fobj.write("Total duplicate files deleted : " + str(DuplicateCount) + "\n")
#     fobj.close()


# def main():
#     if len(sys.argv) != 2:
#         print("Directory name please")
#         return
#     DirectoryScanner(sys.argv[1])
# if __name__ == "__main__":
#     main()


# 4) Design automation script which accepts directory name and delete all duplicate files from that 
# directory. Write names of duplicate files from that directory into log file named as Log.txt. 
# Log.txt file should be created into current directory. Display execution time required for the script

import sys
import os
import hashlib
import time

def DirectoryScanner(DirName):

    if not os.path.exists(DirName):
        print("There is no such directory")
        return

    if not os.path.isdir(DirName):
        print("It is not a directory")
        return

    fobj = open("Log.txt", "w")

    FileDict = {}
    TotalFiles = 0
    DuplicateCount = 0

    for FolderName, SubFolder, FileNames in os.walk(DirName):
        for fname in FileNames:
            TotalFiles += 1
            FilePath = os.path.join(FolderName, fname)

            hobj = hashlib.md5()
            f = open(FilePath, "rb")
            hobj.update(f.read())
            f.close()

            FileHash = hobj.hexdigest()

            if FileHash in FileDict:
                fobj.write("Duplicate file deleted : " + FilePath + "\n")
                os.remove(FilePath)
                DuplicateCount += 1
            else:
                FileDict[FileHash] = FilePath

    fobj.write("\nTotal files scanned : " + str(TotalFiles) + "\n")
    fobj.write("Total duplicate files deleted : " + str(DuplicateCount) + "\n")
    fobj.close()


def main():
    if len(sys.argv) != 2:
        print("Directory name please")
        return

    StartTime = time.time()
    DirectoryScanner(sys.argv[1])
    EndTime = time.time()

    print("Time required : ",EndTime-StartTime,"seconds")
if __name__ == "__main__":
    main()
