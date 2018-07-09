import pandas
import numpy as np
from keras.utils import np_utils
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

##############################################################################################################################################

d = pandas.read_csv("wine.txt",names=["Class","Alcohol","Malic Alic","Ash","Alcanility of Ash","Magnesium",
                    "Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280_OD315_diluted wines",
                    "Proline"])

y = d["Class"].values
#One-hot matrix (binary matrix)
y = np_utils.to_categorical(y)
y = y[:,1:4]
#Remove why because this is what we trying to predict
del(d["Class"])
d = d.values

print(y)

# ##############################################################################################################################################

model = Sequential()
# 13 inputs to 40 neurons
model.add(Dense(40, input_dim=13, init='normal', activation='relu'))
# anther layer 10 neurons
model.add(Dense(10, init='normal',activation="sigmoid"))
model.add(Dropout(0.10))
model.add(Dense(5, init='normal',activation="sigmoid"))
#3 outputs
model.add(Dense(3, init='normal',activation="softmax"))

sgd = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)

#ategorical_crossentropy very good for classification
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=["acc"])

model.fit(d,y,nb_epoch=1600,verbose=1)

score = model.evaluate(d, y, verbose=0)

print(score)
# ##############################################################################################################################################
