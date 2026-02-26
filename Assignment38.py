import pandas as pd 
import matplotlib.pyplot as plt
dataset = "student_performance_ml.csv"

df = pd.read_csv(dataset)

########################
# Que 1
########################
print("\nFirst 5 record : ")
print(df.head())

print("\nLast 5 record : ")
print(df.tail())

print("\nCount of rows is : ",df.shape[0])
print("\nCount of column is : ",df.shape[1])

print("\nList of column names : ",list(df.columns))
print("\nData types of each column : ",list(df.dtypes))

########################
# Que 2
########################
print("Total number of student in the dataset is : ",df.shape[0])

passed = (df["FinalResult"]==1).sum()
print("Total number of passed student : ",passed)

failed = (df["FinalResult"]==0).sum()
print("Total number of failed student : ",failed)

########################
# Que 3
########################
print("Average StudyHours : ",df["StudyHours"].mean())

print("Average Attendance : ",df["Attendance"].mean())

print("Maximum PreviousScore : ",df["PreviousScore"].max())

print("Minimum SleepHours :",df["SleepHours"].min())

########################
# Que 4
########################
vc = df["FinalResult"].value_counts()
print(vc)

########################
# Que 5
########################
print("\nDistribution of FinalResult : ")
counts = df["FinalResult"].value_counts()
print(counts)

percentage = df["FinalResult"].value_counts(normalize=True)*100
print("\nPercentage is : ",percentage)

########################
# Que 6
########################
# Student with higher studyhours genrally have passed.
# Students with low study hours mostly fail.
# Higher attendace show better passing ratrio.
# Therefore, Study hours and attendance positively affect performance.

########################
# Que 7
########################
plt.hist(df["StudyHours"])
plt.xlabel("Study Hours")
plt.ylabel("Number of students")
plt.title("Distribution of study hours")
plt.show()

########################
# Que 8
########################

plt.scatter(df[df["FinalResult"]==1]["StudyHours"],
            df[df["FinalResult"]==1]["PreviousScore"],
            label="Pass")

plt.scatter(df[df["FinalResult"]==0]["StudyHours"],
            df[df["FinalResult"]==0]["PreviousScore"],
            label="Fail")

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.legend()
plt.show()

########################
# Que 9
########################
plt.boxplot(df["Attendance"])
plt.title("Boxplot of Attendance")
plt.show()

########################
# Que 10
########################
plt.scatter(df["AssignmentsCompleted"],df["FinalResult"])
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")
plt.show()
# More assignment completed ->  higher chance of Pass
# Students completing fewer asignments mostly fail.

plt.scatter(df["SleepHours"],df["FinalResult"])
plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")
plt.show()