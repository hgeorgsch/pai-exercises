from tensorflow import keras
from tensorflow.python.keras.layers import Dense

model = keras.Sequential([  
  Dense(units=1, input_dim=1)  
])


import numpy as np
x = np.array([[5]])
y = model(x)
print( x, y )

w1,b1 = model.layers[0].get_weights()
print(w1)
print(b1)

w1[0,0] = 0

model.layers[0].set_weights( [ w1, b1 ] ) 


y = model(x)
print( x, y )
