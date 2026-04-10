# Q.7) Write a python program using LinearRegression to train a regression model using the dataset below. 
# Study hours = [1,2,3,4,5]
# Marks = [50,55,60,65,70]
# Your program should :
# - Train the regression model
# - Print the coefficient
# - Print the intercept

import numpy as np
from sklearn.linear_model import LinearRegression

Study_Hours = [[1],[2],[3],[4],[5]]
Marks = [50,55,60,65,70]

model = LinearRegression()

model.fit(Study_Hours,Marks)

print("Coefficient is : ",model.coef_[0])
print("Intercept is : ",model.intercept_)

# Q.8) Using the regression model created in the previous question, write a python program to predict marks for 
# 6 study hours and display the predicted value

predicted_marks = model.predict([[6]])
print("Predicted marks is : ",predicted_marks[0])

# Q.9) Consider the dataset below: 
# StudyHours = [1,2,3,4,5]
# SleepHours =  [7,6,7,6,8]
# Marks = [50,55,60,65,70]
# Write a Python program to:
# - Train a regression model using this dataset
# - Print the coefficients for both features
# - Print the intercept

from sklearn.linear_model import LinearRegression

dataX = [
    [1,7],
    [2,6],
    [3,7],
    [4,6],
    [5,8]
]

dataY = [50,55,60,65,70]

model2 = LinearRegression()

model2.fit(dataX,dataY)

print("Coefficient is : ",model2.coef_)
print("Intercept is : ",model2.intercept_)