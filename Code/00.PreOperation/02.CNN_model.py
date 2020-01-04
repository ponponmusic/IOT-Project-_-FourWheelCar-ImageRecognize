# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 13:47:29 2019

@author: ponpon
"""
import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
from keras.models import model_from_json
from keras.models import load_model
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    #tf.enable_eager_execution()
    
    # Opening the files about data
    X = pickle.load(open(r'C:\Users\ponpon\Desktop\iot_file\X.pickle', 'rb'))
    y = pickle.load(open(r'C:\Users\ponpon\Desktop\iot_file\y.pickle', 'rb'))
    
    # normalizing data (a pixel goes from 0 to 255)
    X = X/255.0
    
    # Building the model
    model = Sequential()
    # 3 convolutional layers
    model.add(Conv2D(32, (3, 3), input_shape = X.shape[1:]))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    
    # 2 hidden layers
    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation("relu"))
    
    model.add(Dense(128))
    model.add(Activation("relu"))
    
    # The output layer with 13 neurons, for 13 classes
    model.add(Dense(13))
    model.add(Activation("softmax"))
    
    # Compiling the model using some basic parameters
    model.compile(loss="sparse_categorical_crossentropy",
    				optimizer="adam",
    				metrics=["accuracy"])
    
    # Training the model, with 40 iterations
    # validation_split corresponds to the percentage of images used for the validation phase compared to all the images
    history = model.fit(X, y, batch_size=32, epochs=40, validation_split=0.1)
    
    # Saving the model
    model_json = model.to_json()
    with open('./model.json', "w") as json_file :
    	json_file.write(model_json)
    
    model.save_weights("model.h5")
    print("Saved model weights to disk")
    
    model.save('./CNN.model')
    print("Saved model to disk")
    
    # Printing a graph showing the accuracy changes during the training phase
    print(history.history.keys())
    plt.figure(1)
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    
#    #joblib.dump(model, 'model.sav')
##    filename = 'C:\Users\ponpon\Desktop\iot_file\finalized_model.pickle'
#    pickle_out = open(r'C:\Users\ponpon\Desktop\iot_file\finalized_model.pickle', 'wb')
#    pickle.dump(model, pickle_out)
#    pickle_out.close()
#    #pickle_out = open("model.pickle", "wb")
#    #pickle.dump(model, pickle_out)
#    #pickle.close()
    
    ############
    # load json and create model
    json_file = open('model.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = tf.keras.models.model_from_json(loaded_model_json)
    
    # load weight to the model
    loaded_model.load_weights('model.h5')
    print('load model already!')
    
    # evaluate loaded model on test data
    loaded_model.compile(loss="sparse_categorical_crossentropy",
    				optimizer="adam",
    				metrics=["accuracy"])
    score = loaded_model.evaluate(X, y, verbose=0)
    print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))

    
