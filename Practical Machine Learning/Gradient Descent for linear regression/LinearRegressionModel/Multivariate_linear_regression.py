import numpy as np
import pandas as pd
import sklearn
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

def initialize_parameters(lenw):
    w = np.random.randn(1,lenw)
    b = 0
    return w,b

def forward_prop(X,w,b):
    # X = n*m, y=1*m,z=1*m

    z = np.dot(w,X) + b
    return z

def cost_function(z,y):
    m = y.shape[1]
    J = (1/(2*m)) * np.sum(np.square(z-y))
    return J

def back_prop(X,y,z):
    m = y.shape[1]
    dz = (1/m) * (z-y)
    dw = np.dot(dz,X.T)
    db = np.sum(dz)

    return dw,db

def gradient_descent(w,b,dw,db,learning_rate):
    w = w - learning_rate*dw
    b = b - learning_rate*db

    return w,b

def printValues(i, epochs, cost_train, cost_val):
    print('Epochs: '+str(i)+'/'+str(epochs)+': '+'Training Cost: '+str(cost_train)+' | '+'Validation cost: '+str(cost_val))

def linea_regression(X_train, y_train, X_val, y_val, learning_rate, epochs):
    lenw = X_train.shape[0]
    w,b = initialize_parameters(lenw)

    costs_train = []
    m_train = y_train.shape[1]
    m_val = y_val.shape[1]

    for i in range(1,epochs+1):
        z_train = forward_prop(X_train,w,b)
        cost_train = cost_function(z_train,y_train)

        dw, db = back_prop(X_train,y_train,z_train)
        w,b = gradient_descent(w,b,dw,db,learning_rate)

        if i%10==0:
            costs_train.append(cost_train)

        # cost Validation
        z_val = forward_prop(X_val,w,b)
        cost_val = cost_function(z_val,y_val)

        printValues(i, epochs, cost_train, cost_val)
    
    return w,b


boston = load_boston()
bost = pd.DataFrame(boston['data'])
bost.columns = boston['feature_names']

# Normalize input data
X = (bost - bost.mean()) / (bost.max() - bost.min()) 

y = boston['target']
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.33, random_state=5)

X_train = X_train.T
y_train = np.array([y_train])
X_val = X_val.T
y_val = np.array([y_val])

learning_rate = 0.4
epochs = 500
w,b = linea_regression(X_train, y_train, X_val, y_val, learning_rate, epochs)
print()
print()
print()
print('W: ',w)
print(b)
