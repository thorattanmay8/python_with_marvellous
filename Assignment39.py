import pandas as pd
from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = "-"*80


DatasetPath = "student_performance_ml.csv"

# -------------------------------
# Step 1 : Dataset Loading
# -------------------------------

print(Border)
print("Step 1 : Dataset loading")
print(Border)

df = pd.read_csv(DatasetPath)
print("Dataset gets loaded successfully...")

# -------------------------------
# Step 2 : Data analysis
# -------------------------------

print(Border)
print("Step 2 : Data analysis")
print(Border)

print(df.info())
print("Shape of dataset : ",df.shape)
print("Column names : ",list(df.columns))
print("Missing values (per column) : ",df.isnull().sum())
print("Duplicate rows :", df.duplicated().sum())

print("Class distribution (FinalResult count) : ",df["FinalResult"].value_counts())
print("Statistical report of dataset : ",df.describe())
# -------------------------------
# Step 3 : Data Visualization
# -------------------------------

print(Border)
print("Step 3 : Data Visualization")
print(Border)

features = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]
X = df[features]
Y = df["FinalResult"]

# Scatter plot
plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == sp]
    plt.scatter(temp["StudyHours"],temp["FinalResult"],label = sp)

plt.title("StudyHours vs FinalResult")
plt.xlabel("StudyHours")
plt.ylabel("FinalResult")

plt.legend()
plt.grid(True)
plt.show()

print("Data visualization done successfully")

# -------------------------------
# Step 4 : Train-test split
# -------------------------------

print(Border)
print("Step 4 : Train-test split")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)
print("Dataset splitting activity done")

print("X - Independent : ",X.shape)
print("Y - Independent : ",Y.shape)

print("X_train : ",X_train.shape)
print("X_test : ",X_test.shape)
print("Y_train : ",Y_train.shape)
print("Y_test : ",Y_test.shape)

# -------------------------------
# Step 5 : Model Training
# -------------------------------

print(Border)
print("Step 5 : Model Training")
print(Border)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)
model.fit(X_train,Y_train)
print("Model training completed")

# -------------------------------
# Step 6 : Model Prediction
# -------------------------------

print(Border)
print("Step 6 : Model prediction")
print(Border)

Y_pred = model.predict(X_test)
print("Model evaluation complete")

print(Y_pred.shape)

print("Expected answer : ")
print(Y_test)

print("Predicted answer : ")
print(Y_pred)

# -------------------------------
# Step 7 : Accuracy calculation
# -------------------------------

print(Border)
print("Step 7 : Accuracy calculation")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is : ",accuracy*100)

train_accuracy = model.score(X_train, Y_train)
print("Training Accuracy : ", train_accuracy * 100)

print("Testing Accuracy : ", accuracy * 100)

if train_accuracy > accuracy:
    print("Model may be Overfitting")
elif train_accuracy < accuracy:
    print("Model may be Underfitting")
else:
    print("Model is Balanced")

# -------------------------------------
# Step 8 : Confusion matrix generation
# -------------------------------------

print(Border)
print("Step 8 : Confusion matrix generation")
print(Border)

cm = confusion_matrix(Y_test,Y_pred)
print("Confusion matrix : ",cm)

tn, fp, fn, tp = cm.ravel()

print("True Positive  :", tp)
print("True Negative  :", tn)
print("False Positive :", fp)
print("False Negative :", fn)

# -------------------------------------
# Step 9 : Final Conclusion
# -------------------------------------

print(Border)
print("Step 9 : Final conclusion")
print(Border)

data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
data.plot()

plt.title("Confusion matrix of Student Performance Dataset")
plt.show()

print(Border)
print("Comparing Different Tree Depths")
print(Border)

model1 = DecisionTreeClassifier(max_depth=1, random_state=42)
model1.fit(X_train, Y_train)
acc1 = model1.score(X_test, Y_test)
print("Accuracy with max_depth=1 :", acc1 * 100)

model2 = DecisionTreeClassifier(max_depth=3, random_state=42)
model2.fit(X_train, Y_train)
acc2 = model2.score(X_test, Y_test)
print("Accuracy with max_depth=3 :", acc2 * 100)

model3 = DecisionTreeClassifier(max_depth=None, random_state=42)
model3.fit(X_train, Y_train)
acc3 = model3.score(X_test, Y_test)
print("Accuracy with max_depth=None :", acc3 * 100)

print(Border)
print("Prediction for New Student")
print(Border)

new_student = [[6, 85, 66, 7, 7]]

result = model.predict(new_student)

if result[0] == 1:
    print("The student will PASS")
else:
    print("The student will FAIL")