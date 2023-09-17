import tensorflow as tf
import gensim
import string
import re
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# SETUP
dataset = pd.read_csv('Dataset/insparation.csv')
dataset.drop('Image-link', inplace=True, axis=1)
dataset.drop('Quote-url', inplace=True, axis=1)
dataset.drop('Unnamed: 0', inplace=True, axis=1)

# MODEL 
model = gensim.models.word2vec.load('word2vec_model.binclear')

x = dataset['Category']
y = dataset['Quote']

# TRAIN TEST SPLIT
x_train, x_test,y_train, y_test = train_test_split(x,y, 
                                   random_state=104,
                                   test_size=0.25,
                                   shuffle=True)

# SCALE
scaler = StandardScaler()


print(dataset.head())