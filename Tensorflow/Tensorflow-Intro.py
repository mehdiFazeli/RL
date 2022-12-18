# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-jQWlI7NWSENR8DzpY7MjFzeEEeBgSjc
"""

import numpy as np
import tensorflow as tf

observations = 1000
xs = np.random.uniform(-10, 10, (observations, 1))
zs = np.random.uniform(-10, 10, (observations, 1))
noise = np.random.uniform(-1, 1, (observations, 1))

generated_inputs = np.column_stack((xs, zs))
generated_targets = 2 * xs + 3 * zs + 5 + noise


print (generated_inputs.shape)
print (generated_targets.shape)


np.savez("TF-intro", inputs= generated_inputs, targets = generated_targets)

training_data = np.load('TF-intro.npz')

input_size = 2
output_size = 1

model = tf.keras.Sequential([
    tf.keras.layers.Dense(output_size)
])

model.compile(optimizer= 'sgd', loss='mean_squared_error')
model.fit(training_data['inputs'], training_data['targets'], epochs= 100, verbose= 0)

W = model.layers[0].get_weights()[0]
B = model.layers[0].get_weights()[1]

loss = model.history.history['loss']
print (loss[-1])

print (B)

predict = model.predict_on_batch(training_data['inputs'][:3])
targets = training_data['targets'][:3]
print( predict -  targets)