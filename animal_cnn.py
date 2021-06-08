import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Dense, Flatten
from keras.utils import np_utils
import numpy as np
from numpy.lib.arraypad import pad


classes = ["boar", "crow", "monkey"]
num_classes = len(classes)
image_size = 50

def main():
    X_train, X_test, Y_train, Y_test = np.load('./animal.npy')
    X_train = X_train.astype('float') / 256
    X_test = X_test.astype('float') / 256
    Y_train = np_utils.to_categorical(Y_train, num_classes)
    Y_test = np_utils.to_categorical(Y_test, num_classes)

    model = model_train(X_train, Y_train)
    model_eval(model, X_test, Y_test)

main()
"""
def model_train():
    model = Sequential()
    model.add(Conv2D(32,(3,3), padding='same', input_shape=X_train))
"""