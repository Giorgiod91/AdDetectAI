import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
from SeleniumScript import ad_visible
import numpy as np




# Define the model
model = Sequential()
# input and hidden layer with the default ReLU activation
model.add(Dense(units=8, activation='relu', input_dim=3))  
# hidden layers for later
#model.add(Dense(units=5, activation='relu'))  

# x and y defining
input_features = ad_visible
X = np.array([input_features])

# outpout layer with sigmoid activations since its a binary classification
model.add(Dense(units=1, activation='sigmoid'))


# Compile the model 
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=10)
# Make predictions on new data
predictions = model.predict()
