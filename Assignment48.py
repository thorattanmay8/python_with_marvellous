# Q.1) Write a python program that calculate the mean of a dataset using NumPy for the following values:
# [6,7,8,9,10,11,12]
import numpy as np 
data = [6,7,8,9,10,11,12]
mean = np.mean(data)
print("Mean is : ",mean)

# Q.2) Write a python program that calculates the variance ans standard deviation of the dataset:
# [6,7,8,9,10,11,12]
# Display both result
import numpy as np
data = [6,7,8,9,10,11,12]

variance = np.var(data)
stddev = np.std(data)

print("Variance is : ",variance)
print("Standard deviation is : ",stddev)

# Q.3) Write a python program using standard scaler to perform feature scaling on the following dataset:
# [[25,20000],
#  [30,40000],
#  [35,80000]]
# Print the scaled dataset

from sklearn.preprocessing import StandardScaler
data = [
    [25,20000],
    [30,40000],
    [35,80000]
    ]
model = StandardScaler()

scaled_data = model.fit_transform(data)

print("Scaled data : ")
print(scaled_data)

# Q.4) Write a python program to calculate the euclidean distance between two points before and after applying 
# feature scaling, and explain the difference in results.

import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean

point1 = [25, 20000]
point2 = [35, 80000]

distance_before = euclidean(point1, point2)

data = [point1, point2]
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

scaled_p1 = scaled_data[0]
scaled_p2 = scaled_data[1]

distance_after = euclidean(scaled_p1, scaled_p2)

print("Distance before scaling:", distance_before)
print("Distance after scaling:", distance_after)

# Q.8) Write a python program that calculates TP,TN,FP,Fn for the following arrayas:
# actual = [1,1,1,1,0,0,0,0]
# predicted = [1,1,0,1,0,1,0,0]
# Display all 4 values

from sklearn.metrics import confusion_matrix

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

cm = confusion_matrix(actual, predicted)

TN, FP, FN, TP = cm.ravel()

print("TP:", TP)
print("TN:", TN)
print("FP:", FP)
print("FN:", FN)

# Q.9) Write a python program using scikit-learn to generate a classification report for the following data:
# actual = [1,1,1,1,0,0,0,0]
# predicted = [1,1,0,1,0,1,0,0]
# Display the complete classification report including precision,recall, f1-score, and support.

from sklearn.metrics import classification_report

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

report = classification_report(actual, predicted)

print("Classification Report:\n")
print(report)