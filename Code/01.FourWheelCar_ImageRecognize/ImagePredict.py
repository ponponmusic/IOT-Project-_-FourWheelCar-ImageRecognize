# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:31:19 2019

@author: ponpon
"""
import tensorflow as tf
from keras.models import model_from_json
from keras.preprocessing import image
import cv2
import os
import numpy as np
import warnings
warnings.filterwarnings('ignore')

class ImagePredict():    
       
    def __init__(self):
        
        self.model = self.loadModel()
    
    def loadModel(self):
        
        # load json and create model
        json_file = open('model.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = tf.keras.models.model_from_json(loaded_model_json)
        
        # load weight to the model
        loaded_model.load_weights('model.h5')
        print('load model already!')
        
        return loaded_model
        
    def dataTest(self,path):

        IMG_SIZE = 50
           
        test_image = image.load_img(path, target_size = (IMG_SIZE, IMG_SIZE))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        test_image = np.array(test_image).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

        # class
        CATEGORIES = ['class0','class1']
        
        # predict
        result = self.model.predict(test_image)
        print(result)
        result = list(result[0])
        predict_class = CATEGORIES[result.index(max(result))]
        
        return predict_class

    