# 1) Implement simple linear regression manually without using any ML library

# Dataset
import math
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import mean_squared_error,r2_score

X = [1,2,3,4,5]
Y = [3,4,2,4,5]
    
#-------------------------------
# Mean of X
#-------------------------------
mean_X = sum(X) / len(X)
print("Mean of X = ", mean_X)

#-------------------------------
# Mean of Y
#-------------------------------
mean_Y = sum(Y) / len(Y)
print("Mean of Y = ",mean_Y)

#-------------------------------
# Slope (m)
#-------------------------------
num = 0
denominator = 0

for i in range(len(X)):
    num += (X[i]-mean_X) * (Y[i]-mean_Y)
    denominator += (X[i]-mean_X) ** 2

m = num/denominator
print("Slope (m) = ",m)

#-------------------------------
# Intercept (c)
#-------------------------------
c = mean_Y - (m * mean_X)
print("Intercept (c) = ",c)

#-------------------------------
# Regression equation
#-------------------------------
print("Regression Equation : ")
print(f"Y = {m}X + {c}")
value = float(input("Enter number : "))
y_pred = m * value + c
print(f"Predicted Y for X = {value} : ",y_pred)

# 2) Using the same dataset from above question, calculate model performance.
predicted_val = []
for i in range (len(X)):
    y_pred = m*X[i]+c
    predicted_val.append(y_pred)

print("Actual values : ", Y)
print("Predicted values : ", predicted_val)

mse = mean_squared_error(Y, predicted_val)
print("Mean scuared error is : ",mse)

r2 = r2_score(Y,predicted_val)
print("R2 Score is : ",r2)

Experience = [1,2,3,4,5]
Salary = [20000,25000,30000,35000,40000]

mean_X2 = np.mean(Experience)
mean_Y2 = np.mean(Salary)

num2 = 0
den2 = 0

for i in range(len(Experience)):
    num2 += (Experience[i]-mean_X2)*(Salary[i]-mean_Y2)
    den2 += (Experience[i]-mean_X2)**2

m2 = num2/den2
c2 = mean_Y2 - (m2*mean_X2)

experience = 6
sal = m2 * experience + c2
print("Predicted salary for 6 years experience : ",sal)

plt.scatter(Experience,Salary)
plt.plot(Experience,Salary)
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Linear regression")
plt.show()