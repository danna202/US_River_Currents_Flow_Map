from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/river_flow_data')
def river_flow_data():
    # Example: Fetch river flow data from USGS NWIS API
    api_url = 'https://waterservices.usgs.gov/nwis/iv/'
    site = 'site_id'  # Replace with an actual USGS site ID
    parameter = '00060'  # Flow rate parameter code
    format_type = 'json'

    response = requests.get(f'{api_url}?format={format_type}&sites={site}&parameterCd={parameter}')
    data = response.json()
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
