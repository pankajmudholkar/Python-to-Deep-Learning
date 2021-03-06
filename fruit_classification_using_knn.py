# -*- coding: utf-8 -*-
"""Fruit Classification using KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UofsbmXfhJ7RF5azUOc_LDvuNBj89gAZ
"""

import pandas as pd

df = pd.read_csv('Orange vs Grapefruit.csv')
df

df.shape

# Exploratory Data Analysis

df.describe()

df.columns

fname = df['name'].unique()
fname

type(fname)

fsize = df.groupby('name',sort=False).size()
fsize

type(fsize)

import matplotlib.pyplot as plt
plt.bar(fname,fsize,color = ['orange','y'])
plt.xlabel('Fruit Name')
plt.ylabel('Fruit Count')
plt.title('Fruits with Color Dataset')
plt.show()

from mpl_toolkits.mplot3d import axes3d # Library
fig = plt.figure() # 
ax = fig.add_subplot(111,projection='3d') 
ax.scatter(df['red'],df['green'],df['blue'])
ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')
plt.show()

df.head(5)

x = df.iloc[:,[1,2,3,4,5]].values
y = df.iloc[:,0].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state = 0)

train_test_split?

print(x_train.shape)
print(x_test.shape)# 75:25

# Normalization using Min Max - 0 to 1
# It is done only for input
from sklearn.preprocessing import MinMaxScaler
s = MinMaxScaler()
x_train = s.fit_transform(x_train) # fit_transform for training
x_test = s.transform(x_test) # transform for testing

x_train

x_test

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 7)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
y_pred

y_test

from sklearn.metrics import accuracy_score,confusion_matrix
accuracy_score(y_pred,y_test)*100

confusion_matrix(y_pred,y_test)

model.score(x_test,y_test)*100

from sklearn.metrics import classification_report
print(classification_report(y_pred,y_test))

ypred1 = model.predict(s.transform([[2.96,86.76,172,85,2]])) # Testing data

ypred1

ypred1 = model.predict(s.transform([[15.35,253.89,149,77,20]])) # Testing data

ypred1

ypred1 = model.predict(s.transform([[10,150,152,80,10]])) # Testing data
ypred1