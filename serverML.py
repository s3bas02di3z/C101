#Python Libraries 
from flask import Flask, request, jsonify, render_template
import numpy as np
from load import joblib
import os 
from werkzeug.utils import secure_filename

#Load model
dt = joblib.load('dt1_ml.joblib')
#Create Flask App
server = Flask(__name__)

#Define route
@server.route('/predictjson', methods=['POST'])