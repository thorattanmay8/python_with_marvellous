# ---------------------------------------------
# Step 1: Import Libraries
# ---------------------------------------------
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# ---------------------------------------------
# Step 2: Load Dataset
# ---------------------------------------------
df = pd.read_csv("student_performance_ml.csv")

print("First 5 Records:\n", df.head())

# ---------------------------------------------
# Step 3: Define Features and Target
# ---------------------------------------------
X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

# ---------------------------------------------
# Step 4: Train-Test Split
# ---------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------------
# Step 5: Train Decision Tree Model
# ---------------------------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("\nFull Feature Model Accuracy:", accuracy)

# ==========================================================
# Feature Importance
# ==========================================================
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance:\n", importance)

# ==========================================================
# Remove SleepHours and Retrain
# ==========================================================
X2 = df.drop(["FinalResult", "SleepHours"], axis=1)

X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2, y, test_size=0.2, random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X2_train, y2_train)

y2_pred = model2.predict(X2_test)

accuracy2 = accuracy_score(y2_test, y2_pred)
print("\nAccuracy Without SleepHours:", accuracy2)

# ==========================================================
# Train Using Only StudyHours and Attendance
# ==========================================================
X3 = df[["StudyHours", "Attendance"]]

X3_train, X3_test, y3_train, y3_test = train_test_split(
    X3, y, test_size=0.2, random_state=42
)

model3 = DecisionTreeClassifier(random_state=42)
model3.fit(X3_train, y3_train)

y3_pred = model3.predict(X3_test)

accuracy3 = accuracy_score(y3_test, y3_pred)
print("\nAccuracy Using Only StudyHours & Attendance:", accuracy3)

# ==========================================================
# Predict 5 New Students
# ==========================================================
new_students = pd.DataFrame({
    "StudyHours": [5, 2, 7, 4, 1],
    "Attendance": [85, 60, 95, 75, 50],
    "PreviousScore": [78, 40, 88, 65, 35],
    "AssignmentsCompleted": [8, 3, 10, 6, 2],
    "SleepHours": [7, 6, 8, 7, 5]
})

predictions = model.predict(new_students)

print("\nPredictions for New Students:")
for i, pred in enumerate(predictions):
    result = "Pass" if pred == 1 else "Fail"
    print(f"Student {i+1}: {result}")

# ==========================================================
# Manual Accuracy Calculation
# ==========================================================
correct = np.sum(y_test == y_pred)
manual_accuracy = correct / len(y_test)

print("\nManual Accuracy:", manual_accuracy)
print("Sklearn Accuracy:", accuracy)

# ==========================================================
# Misclassified Students
# ==========================================================
misclassified = X_test[y_test != y_pred]
print("\nMisclassified Students:\n", misclassified)
print("Total Misclassified:", len(misclassified))

# ==========================================================
# # Different Random States
# ==========================================================
for rs in [0, 10, 42]:
    X_train_rs, X_test_rs, y_train_rs, y_test_rs = train_test_split(
        X, y, test_size=0.2, random_state=rs
    )
    
    model_rs = DecisionTreeClassifier(random_state=rs)
    model_rs.fit(X_train_rs, y_train_rs)
    
    y_pred_rs = model_rs.predict(X_test_rs)
    acc_rs = accuracy_score(y_test_rs, y_pred_rs)
    
    print(f"\nAccuracy with random_state={rs}:", acc_rs)

# ==========================================================
# # Decision Tree Visualization
# ==========================================================
plt.figure(figsize=(15,8))
plot_tree(model, feature_names=X.columns, class_names=["Fail", "Pass"], filled=True)
plt.title("Decision Tree Visualization")
plt.show()

# ==========================================================
# # Add Performance Index Feature
# ==========================================================
df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

X4 = df.drop("FinalResult", axis=1)
y4 = df["FinalResult"]

X4_train, X4_test, y4_train, y4_test = train_test_split(
    X4, y4, test_size=0.2, random_state=42
)

model4 = DecisionTreeClassifier(random_state=42)
model4.fit(X4_train, y4_train)

y4_pred = model4.predict(X4_test)
accuracy4 = accuracy_score(y4_test, y4_pred)

print("\nAccuracy After Adding PerformanceIndex:", accuracy4)

# ==========================================================
# max_depth=None (Overfitting Check)
# ==========================================================
model5 = DecisionTreeClassifier(max_depth=None, random_state=42)
model5.fit(X_train, y_train)

train_pred = model5.predict(X_train)
test_pred = model5.predict(X_test)

train_accuracy = accuracy_score(y_train, train_pred)
test_accuracy = accuracy_score(y_test, test_pred)

print("\nTraining Accuracy (max_depth=None):", train_accuracy)
print("Testing Accuracy (max_depth=None):", test_accuracy)