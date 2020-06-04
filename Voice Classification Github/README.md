# Gender Classifier

A Python web based dextop application that selects an existing audio file from the system and classifies it into male or female. It is made using keras and deployed using the FLASK framework.

## Getting Started

Before running the project,follow the following steps:<br>
1.Download " train-clean-100.tar.gz [6.3G]   (training set of 100 hours "clean" speech ) " data from http://www.openslr.org/12/
2.Extract the data inside the "Gender_Classifier" folder and rename it to "LibriSpeechTrain"                                            
3.Download " test-clean.tar.gz [346M]   (test set, "clean" speech ) " data from http://www.openslr.org/12/
4.Extract the data inside the "Gender_Classifier" folder and rename it to "LibriSpeechTest"                                            
5.Change the path to directories in directory_management.ipynb and run it.                       
6.Run the Gender_Classifier_NN.ipynb to extract data,preprocess data, train model and store trained model.

### Prerequisites
You will need Python 3.x, Keras.
Python 3.x can be downloaded from https://www.python.org/downloads/

### Instaling
* keras
```
pip install keras
```
* pandas
```
pip install pandas
```
* numpy
```
pip install numpy
```
* matplotlib
```
pip install matplotlib
```
* sklearn
```
pip install scikit-learn
```

## Deployment
1. Go to the project sub direcory and open cmd or anaconda prompt where you have installed all the libraries.
2. Run the commands
* set FLASK_APP=predict_app.py
* flask run --host=0.0.0.0
3. Go to static subdirectory inside the project and run ined_new.html
4. click on choose file and got to directory code/audio_files and select an audio for classification
5. click on predict button

## Contributing

Please read [CONTRIBUTING.md] for details on our code of conduct, and the process for submitting pull requests to us.

## Built With

* Python 3.x
* Jupyter notebook
* FLASK

## Authors

**Mukul Verma**
