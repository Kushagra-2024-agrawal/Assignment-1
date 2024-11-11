from flask import Flask, render_template, request
import pandas as pd
import os
import plotly.express as px
from job_analysis import analyze_job_data  # Function for analysis

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle file upload and analysis
@app.route('/analyze', methods=['POST'])
def analyze_file():
    if 'file' not in request.files:
        return "No file part in the request"
    file = request.files['file']
    if file.filename == '':
        return "No file selected"
    
    # Save the uploaded file
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)
    
    # Load and analyze the data
    data = pd.read_csv(file_path)
    analysis_results, figures = analyze_job_data(data)
    
    # Return the analysis results
    return render_template('result.html', analysis_results=analysis_results, figures=figures)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
