from flask import Flask, render_template, request, jsonify, send_from_directory
import requests

app = Flask(__name__)
GOOGLE_MAPS_API_KEY = 'AIzaSyDqlgjgW4XiLsJM33jY8voBIjGUQswKd_I' 

@app.route('/')
def index():
    return render_template('index.html', google_maps_api_key=GOOGLE_MAPS_API_KEY)

@app.route('/geocode')
def geocode():
    address = request.args.get('address')
    data = geocode_address(address, GOOGLE_MAPS_API_KEY)
    return jsonify(data)

@app.route('/directions')
def directions():
    start = request.args.get('start')
    end = request.args.get('end')
    data = get_directions(start, end, GOOGLE_MAPS_API_KEY)
    return jsonify(data)

def geocode_address(address, api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json"
    params = {'address': address, 'key': api_key}
    response = requests.get(url, params=params)
    return response.json()

def get_directions(start, end, api_key):
    url = f"https://maps.googleapis.com/maps/api/directions/json"
    params = {
        'origin': start,
        'destination': end,
        'key': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
