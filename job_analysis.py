import pandas as pd
import plotly.express as px

def analyze_job_data(data):
    # Example: Basic analysis of job titles and locations
    job_counts = data['job_title'].value_counts().head(10)
    location_counts = data['location'].value_counts().head(10)
    
    # Create figures using Plotly
    fig_jobs = px.bar(job_counts, title='Top 10 Job Titles')
    fig_locations = px.bar(location_counts, title='Top 10 Locations')
    
    # Convert figures to HTML
    job_fig_html = fig_jobs.to_html(full_html=False)
    location_fig_html = fig_locations.to_html(full_html=False)
    
    # Analysis results summary
    analysis_results = {
        'total_jobs': len(data),
        'top_job_titles': job_counts.to_dict(),
        'top_locations': location_counts.to_dict()
    }
    
    return analysis_results, [job_fig_html, location_fig_html]
