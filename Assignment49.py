# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("diabetes.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Column info
print("\nColumn Info:")
df.info()

# Check null values
print("\nNull values:")
print(df.isnull().sum())

# Basic statistics
print("\nStatistics:")
print(df.describe())


# =========================
# EDA (Graphs)
# =========================

# Target variable distribution
sns.countplot(x=df['Outcome'])
plt.title("Outcome Distribution")
plt.show()

# Histogram
df.hist(figsize=(10,8))
plt.show()

# Boxplot
sns.boxplot(data=df)
plt.xticks(rotation=45)
plt.show()


# =========================
# Data Preprocessing
# =========================

# Replace 0 values with mean (simple way)
df['Glucose'] = df['Glucose'].replace(0, df['Glucose'].mean())
df['BloodPressure'] = df['BloodPressure'].replace(0, df['BloodPressure'].mean())
df['BMI'] = df['BMI'].replace(0, df['BMI'].mean())

# Split data
X = df.drop('Outcome', axis=1)
y = df['Outcome']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# =========================
# Model Building
# =========================

# Logistic Regression
from sklearn.linear_model import LogisticRegression
model1 = LogisticRegression()
model1.fit(X_train, y_train)

# KNN
from sklearn.neighbors import KNeighborsClassifier
model2 = KNeighborsClassifier()
model2.fit(X_train, y_train)

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
model3 = DecisionTreeClassifier()
model3.fit(X_train, y_train)


# =========================
# Prediction
# =========================

y_pred1 = model1.predict(X_test)
y_pred2 = model2.predict(X_test)
y_pred3 = model3.predict(X_test)


# =========================
# Evaluation
# =========================

from sklearn.metrics import accuracy_score, confusion_matrix

print("\nLogistic Regression Accuracy:", accuracy_score(y_test, y_pred1))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred1))

print("\nKNN Accuracy:", accuracy_score(y_test, y_pred2))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred2))

print("\nDecision Tree Accuracy:", accuracy_score(y_test, y_pred3))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred3))


# =========================
# Final Output
# =========================

print("\nSample Predictions:")
print(y_pred1[:10])