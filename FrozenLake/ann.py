#! /usr/bin/env python3
import numpy as np   
import tensorflow as tf
from tensorflow import keras  
from tensorflow.python.keras.layers import Dense

x_data = np.linspace(0, 15, 16)
normalizer = keras.layers.Normalization(input_shape=[1,], axis=None)  
normalizer.adapt(np.array(x_data))

model = keras.Sequential([  
	 normalizer,  
	 Dense(64, activation='relu'),  
	 Dense(64, activation='relu'),  
	 Dense(4)  
])  

model.compile(  
    optimizer=tf.optimizers.Adam(learning_rate=0.001),  
	  loss='mse'  
)

y_data = np.array([
	[0.54, 0.53, 0.53, 0.52],
	[0.34, 0.33, 0.32, 0.50],
	[0.44, 0.43, 0.42, 0.47],
	[0.31, 0.31, 0.30, 0.46],
	[0.56, 0.38, 0.37, 0.36],
	[0., 0., 0., 0.],
	[0.36, 0.2, 0.36, 0.16],
	[0., 0., 0., 0.],
	[0.38, 0.41, 0.40, 0.59],
	[0.44, 0.64, 0.45, 0.40],
	[0.62, 0.50, 0.40, 0.33],
	[0., 0., 0., 0.],
	[0., 0., 0., 0.],
	[0.46, 0.53, 0.74, 0.50],
	[0.73, 0.86, 0.82, 0.78],
	[1, 1, 1, 1]
])

model.fit(
	x_data,
	y_data,
	epochs=50000,
	verbose=0)

y = model(x_data)
print( y_data )
print( y )
print( y_data-y )
