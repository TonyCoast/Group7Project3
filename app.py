import json
import pandas as pd
from flask import Flask, jsonify

#################################################
# Data Setup
#################################################

# Define the file paths for the CSV files
file_paths = {
    'Alcohol_Atlanta': '/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/Group_7_Project_3/Group7Project3/CPI Data/Alcohol_Atlanta.csv',
    'Alcohol_Chicago': '/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/Group_7_Project_3/Group7Project3/CPI Data/Alcohol_Chicago.csv',
    'Alcohol_Denver': '/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/Group_7_Project_3/Group7Project3/CPI Data/Alcohol_Denver.csv',
    'Dairy_Atlanta': '/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/Group_7_Project_3/Group7Project3/CPI Data/Dairy_Atlanta.csv',
    'Dairy_Chicago': '/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/Group_7_Project_3/Group7Project3/CPI Data/Dairy_Chicago.csv',
    'Dairy_Denver': '/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/Group_7_Project_3/Group7Project3/CPI Data/Dairy_Denver.csv',
    'Meats_Atlanta': '/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/Group_7_Project_3/Group7Project3/CPI Data/Meats_Atlanta.csv',
    'Meats_Chicago': '/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/Group_7_Project_3/Group7Project3/CPI Data/Meats_Chicago.csv',
    'Meats_Denver': '/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/Group_7_Project_3/Group7Project3/CPI Data/Meats_Denver.csv',
    'National_CPI': '/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/Group_7_Project_3/Group7Project3/CPI_PPI_Nationally/Merged_CPI_Data.csv',
    'National_PPI': '/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/Group_7_Project_3/Group7Project3/CPI_PPI_Nationally/Merged_PPI_Data.csv'
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

@app.route("/")
def home():
    return (
        f"Welcome to the CPI Data API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation - Precipitation data for the last year<br/>"
        f"/api/v1.0/stations - List of weather stations<br/>"
        f"/api/v1.0/tobs - Temperature observations for the previous year<br/>"
        f"/api/v1.0/start_date - Min, Avg, and Max temperatures from a given start date<br/>"
        f"/api/v1.0/start_date/end_date - Min, Avg, and Max temperatures for a date range<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify(json_data['Alcohol_Atlanta'])

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(json_data['Alcohol_Chicago'])

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(json_data['Alcohol_Denver'])

@app.route("/api/v1.0/<start>")
def start_date(start):
    return jsonify(json_data['Dairy_Atlanta'])

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    return jsonify(json_data['Dairy_Chicago'])

if __name__ == "__main__":
    app.run(debug=True)
