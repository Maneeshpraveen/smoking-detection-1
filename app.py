import numpy as np
import pandas as pd
from flask import Flask, render_template,request
import pickle#Initialize the flask App
app = Flask(__name__,template_folder='templates')
model = pickle.load(open('model1.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():

    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    if prediction == 1:
        pred = "Smoked person"
    elif prediction == 0:
        pred = "Non Smoked person"
    output = pred
    return render_template('index.html', prediction_text='Smoke Detection :{}'.format(output))
if __name__ == "__main__":
    app.run(debug=True)