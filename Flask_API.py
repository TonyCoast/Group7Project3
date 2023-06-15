import os
import json
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

#################################################
# Data Setup
#################################################

# Get the base directory of the project
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define the file paths for the CSV files
file_paths = {
    'Alcohol_Atlanta': os.path.join(base_dir, 'CPI_Data', 'Alcohol_Atlanta.csv'),
    'Alcohol_Chicago': os.path.join(base_dir, 'CPI_Data', 'Alcohol_Chicago.csv'),
    'Alcohol_Denver': os.path.join(base_dir, 'CPI_Data', 'Alcohol_Denver.csv'),
    'Dairy_Atlanta': os.path.join(base_dir, 'CPI_Data', 'Dairy_Atlanta.csv'),
    'Dairy_Chicago': os.path.join(base_dir, 'CPI_Data', 'Dairy_Chicago.csv'),
    'Dairy_Denver': os.path.join(base_dir, 'CPI_Data', 'Dairy_Denver.csv'),
    'Meats_Atlanta': os.path.join(base_dir, 'CPI_Data', 'Meats_Atlanta.csv'),
    'Meats_Chicago': os.path.join(base_dir, 'CPI_Data', 'Meats_Chicago.csv'),
    'Meats_Denver': os.path.join(base_dir, 'CPI_Data', 'Meats_Denver.csv'),
    'National_CPI_PPI': os.path.join(base_dir, 'cpi_ppi_merged.csv')
}

# Load the CSV files and convert to JSON
json_data = {}
for data_name, file_path in file_paths.items():
    df = pd.read_csv(file_path)
    json_data[data_name] = df.to_dict(orient='records')

#################################################
# Flask Setup
#################################################

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def home():
    return (
        f"Welcome to the CPI Data API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/Alcohol_Atlanta - CPI for alcohol in Atlanta<br/>"
        f"/api/v1.0/Alcohol_Chicago - CPI for alcohol in Chicago<br/>"
        f"/api/v1.0/Alcohol_Denver - CPI for alcohol in Denver<br/>"
        f"/api/v1.0/Dairy_Atlanta - CPI for dairy in Atlanta<br/>"
        f"/api/v1.0/Dairy_Chicago - CPI for dairy in Chicago<br/>"
        f"/api/v1.0/Dairy_Denver - CPI for dairy in Denver<br/>"
        f"/api/v1.0/Meats_Atlanta - CPI for meats in Atlanta<br/>"
        f"/api/v1.0/Meats_Chicago - CPI for meats in Chicago<br/>"
        f"/api/v1.0/Meats_Denver - CPI for meats in Denver<br/>"
        f"/api/v1.0/National_CPI_PPI - National CPI and PPI data<br/>"
    )

@app.route("/api/v1.0/Alcohol_Atlanta")
def alcohol_atlanta():
    return jsonify(json_data['Alcohol_Atlanta'])

@app.route("/api/v1.0/Alcohol_Chicago")
def alcohol_chicago():
    return jsonify(json_data['Alcohol_Chicago'])

@app.route("/api/v1.0/Alcohol_Denver")
def alcohol_denver():
    return jsonify(json_data['Alcohol_Denver'])

@app.route("/api/v1.0/Dairy_Atlanta")
def dairy_atlanta():
    return jsonify(json_data['Dairy_Atlanta'])

@app.route("/api/v1.0/Dairy_Chicago")
def dairy_chicago():
    return jsonify(json_data['Dairy_Chicago'])

@app.route("/api/v1.0/Dairy_Denver")
def dairy_denver():
    return jsonify(json_data['Dairy_Denver'])

@app.route("/api/v1.0/Meats_Atlanta")
def meats_atlanta():
    return jsonify(json_data['Meats_Atlanta'])

@app.route("/api/v1.0/Meats_Chicago")
def meats_chicago():
    return jsonify(json_data['Meats_Chicago'])

@app.route("/api/v1.0/Meats_Denver")
def meats_denver():
    return jsonify(json_data['Meats_Denver'])

@app.route("/api/v1.0/National_CPI_PPI")
def national_cpi():
    return jsonify(json_data['National_CPI_PPI'])

if __name__ == "__main__":
    app.run(debug=True)

