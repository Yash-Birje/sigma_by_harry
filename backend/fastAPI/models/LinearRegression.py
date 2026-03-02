import pandas as pd
import numpy as np

def gradient_descent(X, Y, w, b, learning_rate, iterations, regularization=None, lambda_=0.01):
    
    m = X.shape[0]
    
    for i in range(iterations):
        
        Y_pred = np.dot(X, w) + b
        
        loss = (1/(2*m)) * np.sum((Y_pred - Y) ** 2)

        if(regularization == "L1"):
            loss += lambda_ * np.sum(np.abs(w))
        elif(regularization == "L2"):
            loss += lambda_ * np.sum(w ** 2)
        
        dw = (1/m) * np.dot(X.T, (Y_pred - Y))
        
        if(regularization == "L1"):
            dw += lambda_ * np.sign(w)
        elif(regularization == "L2"):
            dw += 2 * lambda_ * w
        
        db = (1/m) * np.sum(Y_pred - Y)
        
        w -= learning_rate * dw
        b -= learning_rate * db
        
        if i % 100 == 0:
            print(f"Iteration {i}, Loss: {loss:.5f}, w: {w}, b: {b}")
            print('_'*80)
    
    return w, b

# import numpy as np

def LinearRegression(df, target_column,learning_rate=0.01, iterations=1000,regularization=None, lambda_=0.01):
    
    # Separate features and target
    X = df.drop(columns=[target_column]).to_numpy()
    Y = df[target_column].to_numpy().reshape(-1, 1)
    
    m, n = X.shape
    
    # Initialize parameters properly
    w = np.ones((n, 1))
    b = 0.0
    
    w, b = gradient_descent(X, Y, w, b, learning_rate, iterations, regularization, lambda_)
    
    return w, b

df = pd.DataFrame({
    "x1": [1,2,3,4,5,5,4,2,3,4,5,8,9,111,11],
    "x2": [15,2,3,4,5,6,5,6,8,9,10,12,15,10,9],
    "y":  [31,5,6,9,12,15,17,14,14,19,25,32,39,131,29]
})

w, b = LinearRegression(df, "y", learning_rate=0.0001, iterations=5000, lambda_=0.01, regularization="L1")
with open("./weights/weights_LinearRegression.json", "w") as f:
  f.write(f"weights: {w.tolist()}, bias: {b}")