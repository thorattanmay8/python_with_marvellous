# 9
# Write a program which accept name from user and display length of its name.
def length(name):
    count = 0
    for i in name:
        count = count+1
    return count

value = length(str(input("Enter name : ")))
print("Length of name is : ",value)