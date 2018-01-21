#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:20:58 2018

@author: josharnold
"""

import pandas as pd
from sklearn.preprocessing import minmax_scale
import os
import numpy as np

class preprocessing:
    
    def load_data():        
        path_dir_train = "data/" + "AID746AID1284red_train.csv"
        path_dir_test = "data/" + "AID746AID1284red_test.csv"
        
        train_data = pd.read_csv(path_dir_train, sep=',', decimal='.')
        test_data = pd.read_csv(path_dir_test, sep=',', decimal='.')
        
        return train_data, test_data
    
    def split_data(train_data, test_data):
        # Separate data into X and y
        X_train = train_data.drop(['Outcome'], axis=1)
        X_test = test_data.drop(['Outcome'], axis=1)
        
        y_train = train_data["Outcome"]
        y_test = test_data["Outcome"]
                        
        # One hot encoding        
        y_train = pd.get_dummies(y_train)
        y_train = y_train.drop(["Inactive"], axis=1)
        
        y_test = pd.get_dummies(y_test)
        y_test = y_test.drop(["Inactive"], axis=1)
        
        return X_train, X_test, y_train, y_test
    
    def scale_data(X_train, X_test, y_train, y_test):
        features_to_avoid = ["Bad", "BBB", "HYP", "ARC", "HBD", "POS", "NEG"]

        for feature in X_train:
            should_scale = True
            for name in features_to_avoid:        
                if (name in feature):
                    should_scale = False 
            if (should_scale):
                X_train[feature] = minmax_scale(X_train[feature])
                
        for feature in X_test:
            should_scale = True
            for name in features_to_avoid:        
                if (name in feature):
                    should_scale = False 
            if (should_scale):
                X_test[feature] = minmax_scale(X_test[feature])
                        
        # Convert to numpy arrays — important for input of data to the deep net
        X_train = X_train.values
        X_test = X_test.values 
        y_train = y_train.values
        y_test = y_test.values   
        
        return X_train, X_test, y_train, y_test
    
class postprocessing:
    
    def create_string_array(data):
        
        array = []
                    
        for i in range(0, len(data)):
            pred = data[i]
            text = str(i+1) + ") " + "Molecule " + str(pred[0]+1) + " binding prediction: " + str(pred[1]) + "\n"
            array.append(text)
        
        return array
    
    def create_tuple_array(data):
        
        array = []
                    
        for i in range(0, len(data)):
            pred = data[i]
            
            bias = 0.01
            result = (pred[0]+1, np.around((pred[1]*100)-bias, decimals=2))
            array.append(result)
        
        return array
        
    def write_output(data):
        
        file_name = "output.txt"
        
        if os.path.exists(file_name):
            os.remove(file_name)
        
        f= open(file_name,"w+")
                    
        for i in range(0, len(data)):
            pred = data[i]
            text = str(i+1) + ") " + "Molecule " + str(pred[0]+1) + " binding prediction: " + str(pred[1]) + "\n"
            f.write(text)
        
        f.close()
        
        
        