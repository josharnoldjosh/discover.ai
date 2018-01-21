#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:20:58 2018

@author: josharnold
"""

"""

AID746 is a primary screen from the Scripps  Research Institute Molecular Screening Center 
for Mitogen-activated protein kinase. 
59,788 compounds were screened with a ratio of 1 active compound to 162 inactive compounds (0.61%). 
57,546 of the compounds screened had known drug-like properties.

"""

from data_module.data import preprocessing, postprocessing
from model import nn
import numpy as np
from flask import Flask
from flask import render_template   
from flask import request

app = Flask(__name__)
   
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/test", methods = ['POST'])
def test():
    if (request.method == 'POST'):
        return "success! " + request.form["hello"]
    else:
        return "Fail!"

@app.route("/predict")
def predict():
    # Seed
    np.random.seed(7)
    
    # Import data
    train, test = preprocessing.load_data()
    
    # Split data
    X_train, X_test, y_train, y_test = preprocessing.split_data(train, test)
    
    # Feature scaling
    X_train, X_test, y_train, y_test = preprocessing.scale_data(X_train, X_test, y_train, y_test)
    
    # Create model
    model = nn.base_model(X_train.shape)
    
    # Train model
    results = nn.train_model(model, X_train, X_test, y_train, y_test)
    
    # Final evaluation / score
    nn.evaluate_model(model, X_test, y_test)
    
    # Output list of predictions
    output_predictions = nn.predict(model, X_test, reverse=True)
    
    # Save output list
    postprocessing.write_output(output_predictions)
        
    print("Script finished!")