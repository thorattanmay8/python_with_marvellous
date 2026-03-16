import pandas as pd 
import numpy as np 

from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def main():
    #---------------------------------------------------
    # Step 1 : Get Data
    #---------------------------------------------------
    df = pd.read_csv("Advertising.csv")
    print("Dataset gets loaded sucessfully...")

    #---------------------------------------------------
    # Step 2 : Clean, Prepare and Manipulate data
    #---------------------------------------------------
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

        print(df.head())
        print("Dataset is cleaned and in well format.")

        print("Checking missing values.")
        print("Missing values count : ",df.isnull().sum())
        
    X = df[['TV','radio','newspaper']]
    Y = df['sales']
    
    #---------------------------------------------------
    # Step 3 : Spliting Dataset for training and testing
    #---------------------------------------------------
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

    print("Shape of X_train : ",X_train.shape)
    print("Shape of X_test : ",X_test.shape)
    print("Dhape of Y_train : ",Y_train.shape)
    print("Shape of Y_test : ",Y_test.shape)

    #---------------------------------------------------
    # Step 4 : Training Model
    #---------------------------------------------------
    model = LinearRegression()

    model.fit(X_train,Y_train)
    print("Model training done successfully.")

    #---------------------------------------------------
    # Step 5 : Testing Model
    #---------------------------------------------------   
    y_pred = model.predict(X_test)

    #---------------------------------------------------
    # Step 6 : Evaluating model
    #---------------------------------------------------  
    MSE = mean_squared_error(Y_test,y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,y_pred)

    print("Mean squared error : ",MSE)
    print("Root mean squared error : ",RMSE)
    print("R square value : ",R2)

    #---------------------------------------------------
    # Step 7 : Compare the actual and predicted values
    #---------------------------------------------------  
    Result = pd.DataFrame({
        'Actual sale' : Y_test.values,
        'Predicted sale' : y_pred
    })
    
    print(Result.head())
    
if __name__ == "__main__":
    main()