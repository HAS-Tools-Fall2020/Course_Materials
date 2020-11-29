# -*- coding: utf-8 -*-
"""
Title: Introduction to some Machine Learning (ML) Methods
@author: Luis De la Fuente

"""
# %% Libraries

import numpy as np #Matrix analysis
import pandas as pd #Dataframe analysis
import matplotlib.pyplot as plt #to Create plots
from datetime import datetime as dt #to convert string to date format
from pathlib import Path #to work with pathfiles
from sklearn.model_selection import train_test_split #to split the dataset
from sklearn.ensemble import RandomForestRegressor #Random Regressor model
from sklearn.neural_network import MLPRegressor #Neural network
from sklearn.preprocessing import StandardScaler #standardization

# %% Initialization

split = 75 #percetange of date used in the trainning. Tradictionally [50-80]

# %% Reading file

file = 'camp_verde_streamflow_precip_temp.csv'  #filename
full_path =  Path(__file__).parent / file   # creating the path = parent path + filename
df = pd.read_csv(full_path) #reading

# %% Preprocessing
df.columns = ['Date', 'T', 'PP', 'Q'] #renaming
df['Date']= pd.to_datetime(df['Date']) #convert object to date format
df['Month'] = df['Date'].dt.month #extracting month as surrogate information
df.index = df['Date'] #storing date as index
df = df.drop('Date', axis=1) #deleting the date information as variable

print(df.describe())
print('\n')
print('The minimum temperature is -32°F...too cold...weird')
print('The maximum precipitation is 729mm...too high...weird')
print('\n')
print('You have to decide what to do with these situations. A good idea is to plot a histograph to watch another problems')

df['T-1'] = df['T'].shift(1) #1 day recursive 
df['PP-1'] = df['PP'].shift(1) #1 day recursive 
df['Q-1'] = df['Q'].shift(1) #1 day recursive, it is your option use the streamflow...pros and cons?
df = df.dropna()


# %% Splitting for Random Forest
X_train_RF, X_test_RF, y_train_RF, y_test_RF = train_test_split(df.drop('Q', axis=1), df.Q, train_size=split/100, shuffle=False) #splitting with a constant period


# %% Random Forest Model (RF)
regr1 = RandomForestRegressor(n_estimators=200, min_samples_split=3, min_samples_leaf=3, max_features=0.5, bootstrap=True)
regr1.fit(X_train_RF, y_train_RF)

print('\n')
print('RF Prediction for T=100, PP=0, Month=10, T-1=100, PP-1=0, Q-1=100:' + str(regr1.predict([[100, 0, 10, 100, 0, 100]]))) #T=100, PP=10, Month=10, T-1=100, PP-1=0, Q-1=0



# %% Splitting for Neural Network
X_train_NN, X_test_NN, y_train_NN, y_test_NN = train_test_split(df.drop('Q', axis=1), df.Q, train_size=split/100, shuffle=False) #splitting with a constant period
scaler = StandardScaler()
scaler.fit(X_train_NN)

y_train_NN = y_train_NN.values.reshape(-1,1)
y_test_NN = y_test_NN.values.reshape(-1,1)
scaler_y = StandardScaler()
scaler_y.fit(y_train_NN)

X_train_NN = scaler.transform(X_train_NN)
X_test_NN = scaler.transform(X_test_NN)
y_train_NN = scaler_y.transform(y_train_NN).ravel()
y_test_NN = scaler_y.transform(y_test_NN).ravel()

# %% Neural Network Model (NN)
regr2 = MLPRegressor(hidden_layer_sizes=(100,8), random_state=1, max_iter=15000)
regr2.fit(X_train_NN, y_train_NN)

print('\n')
print('NN Prediction for T=100, PP=0, Month=10, T-1=100, PP-1=0, Q-1=100:' + str(scaler_y.inverse_transform((regr2.predict(scaler.transform([[100, 0, 10, 100, 0, 100]]))))))