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
from html_parser import text_parser
import numpy as np
from flask import Flask
from flask import render_template   

app = Flask(__name__)
   
@app.route("/")
def main():    
    return render_template("index.html")

@app.route("/upload")
def upload():
    return render_template("uploader.html")

@app.route("/load", methods = ['GET'])
def load():
    return render_template("load.html")

@app.route("/predict", methods = ['GET'])
def get_csv():
    #data = request.form.to_dict() # do something with me (sorry, this is kind of sketch but sacrifices)
    #print(data)

    data = predict()
    
    html = text_parser.create_html(data)    

    # function to create html for final page, then return it    
    return html

def predict(): 
    # Import data
    train, test = preprocessing.load_data()
    
    # Split data
    X_train, X_test, y_train, y_test = preprocessing.split_data(train, test)
    
    # Feature scaling
    X_train, X_test, y_train, y_test = preprocessing.scale_data(X_train, X_test, y_train, y_test)
        
    # Load model
    model = nn.load_model()
    
    # Output list of predictions
    output_predictions = nn.predict(model, X_test, reverse=True)
    
    # Get array of parsed predictions
    result = postprocessing.create_tuple_array(output_predictions)
    
    return result
    

@app.route("/train")
def train():
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
    nn.train_model(model, X_train, X_test, y_train, y_test)
    
    # Final evaluation / score
    nn.evaluate_model(model, X_test, y_test)
    
    # Output list of predictions
    output_predictions = nn.predict(model, X_test, reverse=True)
    
    # Save output list
    postprocessing.write_output(output_predictions)  
    
    # Export model
    nn.export_model(model)
        
    print("Script finished!")
    
    return "Success!"
 
#train()
#predict()