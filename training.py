import random
import pandas as pd
import tensorflow as tf

from sklearn.model_selection import train_test_split

# SETUP
dataset = pd.read_csv('Dataset/insparation.csv')
model = tf.keras.models.Sequential()

dataset.drop('Category', inplace=True, axis=1)
dataset.drop('Image-link', inplace=True, axis=1)
dataset.drop('Quote-url', inplace=True, axis=1)
dataset.drop('Unnamed: 0', inplace=True, axis=1)


x = dataset.drop(columns=['Quote'])
y = dataset["Quote"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) # 20% of the data



# LAYERS
model.add(tf.keras.layers.Dense(256, input_shape=x_train.shape, activation='sigmoid'))
model.add(tf.keras.layers.Dense(256, activation='sigmoid'))

# OUTPUT
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

x_tensor = tf.convert_to_tensor(x_train, dtype=tf.string)
y_tensor = tf.convert_to_tensor(y_train, dtype=tf.string)

model.fit(x_tensor, y_tensor, epochs=10)