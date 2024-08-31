from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the pickled model when the Flask app starts
with open('pickle/xg_final_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from the form data
    item_mrp = float(request.form['item_mrp'])
    outlet_establishment_year = float(request.form['outlet_establishment_year'])
    outlet_size = float(request.form['outlet_size'])
    outlet_location_type = float(request.form['outlet_location_type'])
    outlet_type = float(request.form['outlet_type'])

    # Combine the features into a single numpy array for prediction
    X = np.array([[item_mrp, outlet_establishment_year, outlet_size, outlet_location_type, outlet_type]])

    # Use the model to make a prediction
    prediction = model.predict(X)[0]

    lower_bound = prediction - 714.42
    upper_bound = prediction + 714.42

    # Render result template with prediction and bounds
    return render_template('result.html', 
                           prediction_text=f'Predicted Value: {prediction:.2f}',
                           lower_bound=f'{lower_bound:.2f}',
                           upper_bound=f'{upper_bound:.2f}')
if __name__ == '__main__':
    app.run(debug=True)
