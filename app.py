from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the model
with open('car_price_prediction.model', 'rb') as file:
    model = pickle.load(file)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')  # HTML frontend

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from the request
        data = request.json  # Expecting JSON input
        max_power = float(data['max_power'])
        mileage = float(data['mileage'])
        engine = float(data['engine'])
        
        # Prepare input for prediction
        input_features = [[max_power, mileage, engine]]
        prediction = np.exp(model.predict(input_features)[0])

        # Return prediction
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
