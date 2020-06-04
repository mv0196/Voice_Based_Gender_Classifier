import io
import os
import numpy as np
import pandas as pd
import keras
from keras import backend as K
from keras.models import load_model
from flask import request
from flask import jsonify
from flask import Flask
from flask_cors import CORS, cross_origin
from pickle import load
from tensorflow.keras.models import load_model
import librosa

app=Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/predict": {"origins": "http://localhost:port"}})

def get_model():
	global model
	model=load_model("D:\\Voice Classification\\Code\\Gender_Classifier\\trained_models\\Gender_Classifier_NN.h5")
	print("* Model Loaded")


def extract_features(files):
	
	file_name="D:\\Voice Classification\\Code\\project\\audio_files\\"+files.file

	X, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 

	mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)

	stft = np.abs(librosa.stft(X))

	chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)

	mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)

	contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)

	tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X),sr=sample_rate).T,axis=0)
	
	return mfccs, chroma, mel, contrast, tonnetz

def preprocess(path):
	features=pd.DataFrame({"file":[path]}).apply(extract_features,axis=1)
	x=np.array(features)
	features_new_test = []
	for i in range(0, len(x)):
		features_new_test.append(np.concatenate((x[i][0], x[i][1], x[i][2], x[i][3], x[i][4]), axis=0))
	X_new_test = np.array(features_new_test)
	ss = load(open('D:\\Voice Classification\\Code\\Gender_Classifier\\scaler.pkl', 'rb'))
	X_new_test_scaled = ss.transform(X_new_test)
	return X_new_test_scaled
					   
print("* Loading Keras Model")
get_model()

@app.route('/predict', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def predict():
	message = request.get_json(force=True)#just for formality
	path=message['audio']
	scaled_data=preprocess(path)
	prediction = model.predict_classes(scaled_data)
	response = {
		'prediction': {
			'male': 0,
			'female': 0
		}
	}
	if prediction[0]==1:
		response['prediction']['male']=1
	elif prediction[0]==0:
		response['prediction']['female']=1
	return jsonify(response)
