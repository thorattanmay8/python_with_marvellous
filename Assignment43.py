import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():

    #----------------------------------------------
    # step 1 : Load the dataset
    #----------------------------------------------
    df = pd.read_csv("PlayPredictor.csv")
    print("Dataset gets loaded successfully...")

    #----------------------------------------------
    # Step 2 : Clean, prepare and manipulate data
    #----------------------------------------------
    le = LabelEncoder()

    df['Whether'] = le.fit_transform(df['Whether'])
    df['Temperature'] = le.fit_transform(df['Temperature'])
    df['Play'] = le.fit_transform(df['Play'])

    # Defining features and labels 
    features = [
        "Whether",
        "Temperature"
    ]
    X = df[features]
    Y = df["Play"]

    #----------------------------------------------
    # Step 3 : Spliting data
    #----------------------------------------------
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,random_state=42)

    print("X - Independent : ",X.shape)
    print("Y - Independent : ",Y.shape)

    print("X_train : ",X_train.shape)
    print("X_test : ",X_test.shape)
    print("Y_train : ",Y_train.shape)
    print("Y_test : ",Y_test.shape)

    #----------------------------------------------
    # Step 4 : Traning Data
    #----------------------------------------------
    model = KNeighborsClassifier()
    
    model.fit(X_train,Y_train)

    print("Model traning completed")

    #----------------------------------------------
    # Step 5 : Testing Data
    #----------------------------------------------

    Y_pred = model.predict(X_test)

    CheckAccuracy(Y_test,Y_pred)

def CheckAccuracy(Y_test,Y_pred):
    #----------------------------------------------
    # Step 6 : Calculate Accuracy
    #----------------------------------------------
    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy score of our model is : ",accuracy*100)

if __name__ == "__main__":
    main()