from flask import Flask, request, jsonify
from flask_cors import CORS 
import util

app = Flask(__name__)
CORS(app)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Orgin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        response = jsonify({
            'estimated_prices': estimated_price
        })
    except Exception as e:
        response = jsonify({
            'error': str(e)
        })
    return response



if __name__ == "__main__":
    print("Starting Python flask Server for Home Price Production")
    util.load_saved_artifacts() 
    app.run()