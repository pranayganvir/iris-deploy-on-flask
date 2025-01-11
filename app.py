# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    SepalLength = request.form.get('SepalLength')
    SepalLength = float(SepalLength)
    
    SepalWidth = request.form.get('SepalWidth')
    SepalWidth = float(SepalWidth)
    
    PetalLength = request.form.get('PetalLength')
    PetalLength = float(PetalLength)
    
    PetalWidth = request.form.get('PetalWidth')
    PetalWidth = float(PetalWidth)
    # Make prediction
    prediction = model.predict([[SepalLength, SepalWidth, PetalLength, PetalWidth]])
    # output = 'Placed' if prediction[0] == 1 else 'Not Placed'
    output = prediction[0]
    # print(output)
    flowerNames = ["Sesota", "Versicolor", "Virginica"]
    

    return render_template('index.html', prediction_text='Prediction: {}'.format(flowerNames[output]))

if __name__ == "__main__":
    app.run(debug=True)