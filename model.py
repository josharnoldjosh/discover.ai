#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:30:53 2018

@author: josharnold
"""

from settings import param
from keras.models import Sequential 
from keras.layers import Dense, Dropout 
from keras.callbacks import ModelCheckpoint, TensorBoard, EarlyStopping    
from collections import OrderedDict 

class nn:
     
    def base_model(X_shape):
        model = Sequential()
        
        model.add(Dense(activation="relu", input_dim=X_shape[1], units=1000, kernel_initializer="normal"))
        model.add(Dropout(0.2))
        
        model.add(Dense(2100, kernel_initializer="normal", activation="relu"))
        model.add(Dropout(0.3))
           
        model.add(Dense(activation="sigmoid", input_dim=1000, units=1, kernel_initializer="normal"))
        
        model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy","binary_crossentropy"])
        
        return model
    
    def train_model(model, X_train, X_test, y_train, y_test):
        checkpoint = ModelCheckpoint(filepath="best-model.hdf5", monitor='val_acc', verbose=1, save_best_only=True)
        tensorboard = TensorBoard(log_dir='./logs', histogram_freq=0, write_graph=True, write_images=False)
        earlystopping = EarlyStopping(monitor='binary_crossentropy', patience=100, verbose=1, mode='auto') 

        class_weight = {0 : 1.0, 1: 300.0}

        result = model.fit(X_train, y_train, 
                           batch_size=param.batch_size, 
                           epochs=param.epochs, 
                           validation_data=(X_test, y_test), 
                           callbacks=[earlystopping, checkpoint, tensorboard],
                           class_weight = class_weight)
        
        print("Model trained")        
        return result
    
    def evaluate_model(model, X_test, y_test):
        score = model.evaluate(X_test, y_test)
        print('\nTest score:', score[0]) 
        print('Test accuracy:', score[1], "\n")
        
    def predict(model, X_data, reverse=True):
        output_list = model.predict(X_data)
        
        data = {}
        for i in range(0, len(X_data)):
            pred = output_list[i][0]
            data[i] = pred
            
        orded_data = list(OrderedDict(sorted(data.items(), key=lambda kv: kv[1], reverse=reverse)).items())         
        return orded_data
