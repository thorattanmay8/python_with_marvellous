import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay

df = pd.read_csv("bank.csv", sep=',')

print(df.head())

df = df.replace("unknown", "others")

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data Types:\n", df.dtypes)

print("Numerical Stats:\n", df.describe())
print("Categorical Stats:\n", df.describe(include='object'))

df['deposit'] = df['deposit'].map({'yes': 1, 'no': 0})

for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

scaler = StandardScaler()

num_cols = df.select_dtypes(include=['int64', 'float64']).columns
num_cols = num_cols.drop('deposit')   

df[num_cols] = scaler.fit_transform(df[num_cols])

print("Final Data:\n", df.head())

X = df.drop('deposit',axis=1)
Y = df['deposit']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2 ,random_state=42)

log_model = LogisticRegression()
log_model.fit(X_train, Y_train)
log_pred = log_model.predict(X_test)
print("Logistic Accuracy:", accuracy_score(Y_test, log_pred))

knn_model = KNeighborsClassifier()
knn_model.fit(X_train, Y_train)
knn_pred = knn_model.predict(X_test)
print("KNN Accuracy:", accuracy_score(Y_test, knn_pred))

rf_model = RandomForestClassifier()
rf_model.fit(X_train, Y_train)
rf_pred = rf_model.predict(X_test)
print("Random Forest Accuracy:", accuracy_score(Y_test, rf_pred))

models = {
    "Logistic": log_model,
    "KNN": knn_model,
    "Random Forest": rf_model
}

for name, model in models.items():
    print("\n====", name, "====")
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Accuracy
    print("Accuracy:", accuracy_score(Y_test, y_pred))
    
    # Confusion Matrix
    print("Confusion Matrix:\n", confusion_matrix(Y_test, y_pred))
    
    # Classification Report
    print("Classification Report:\n", classification_report(Y_test, y_pred))
    
    # ROC-AUC
    y_prob = model.predict_proba(X_test)[:,1]
    print("ROC-AUC:", roc_auc_score(Y_test, y_prob))

models = {
    "Logistic": log_model,
    "KNN": knn_model,
    "Random Forest": rf_model
}

for name, model in models.items():
    ConfusionMatrixDisplay.from_estimator(model, X_test, Y_test)
    plt.title(name + " - Confusion Matrix")
    plt.show()

for name, model in models.items():
    RocCurveDisplay.from_estimator(model, X_test, Y_test)
    plt.title(name + " - ROC Curve")
    plt.show()