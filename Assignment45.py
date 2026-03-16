import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    # Step 1 : Load the dataset from CSV file
    df = pd.read_csv(DataPath)
    print("Some entries from dataset")
    print(df.head())

    # Step 2 : Clean the dataset by removing empty rows
    df.dropna(inplace= True)
    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])

    # Step 3 : Separate independent and dependent variables
    X = df.drop(columns= ['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)
    
    print("Input columns : ",X.columns.to_list)
    print("Output columns : Class")

    # Step 4 : Split the dataset for training and testing
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print("Information of training and testing data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    # Step 5 : Feature Scaling 

    scaler = StandardScaler()
    # Independent variable scaling
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature scaling is done")

    # Step 6 : Explore the multiple values of k 
    # Hyperparameter tuning (K)
    accuracy_scores = []
    K_values = range(1,6)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print("Accuracy report of all k values from 1 to 5")
    for value in accuracy_scores:
        print(value)

    # Step 7 : Plot graph og K vs accuracy 
    plt.figure(figsize=(8,5))
    plt.plot(K_values, accuracy_scores, marker = 'o')
    plt.title("K values vd accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()

def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()