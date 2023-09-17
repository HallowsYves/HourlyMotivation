import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# SETUP
dataset = pd.read_csv('Dataset/insparation.csv')
dataset.drop('Image-link', inplace=True, axis=1)
dataset.drop('Quote-url', inplace=True, axis=1)
dataset.drop('Unnamed: 0', inplace=True, axis=1)

x = dataset['Category']
y = dataset['Quote']

# TRAIN TEST SPLIT
x_train, x_test,y_train, y_test = train_test_split(x,y, 
                                   random_state=104,
                                   test_size=0.25,
                                   shuffle=True)

# X TRAIN
print('X TRAIN : ')
print(x_train.head())

# X TEST
print('X TEST : ')
print(x_test.head())

# Y TRAIN
print('Y TRAIN : ')
print(y_train.head())

# Y TEST
print('Y TEST : ')
print(y_test.head())


print(dataset.head())