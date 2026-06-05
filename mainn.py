from flask import Flask, render_template, jsonify
import pandas as pd
import json
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Sample Sales Data for Accenture
def generate_sales_data():
    dates = [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(30)]
    regions = ['North', 'South', 'East', 'West']
    services = ['Consulting', 'Technology', 'Operations', 'Security']
    
    data = []
    for date in dates:
        for region in regions:
            for service in services:
                data.append({
                    'Date': date,
                    'Region': region,
                    'Service': service,
                    'Sales': random.randint(50000, 500000),
                    'Quantity': random.randint(5, 50)
                })
    
    return pd.DataFrame(data)

df = generate_sales_data()

# Routes
@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    total_sales = df['Sales'].sum()
    total_quantity = df['Quantity'].sum()
    avg_sale = df['Sales'].mean()
    
    return jsonify({
        'total_sales': f"${total_sales:,.0f}",
        'total_quantity': f"{total_quantity:,}",
        'avg_sale': f"${avg_sale:,.0f}",
        'regions': len(df['Region'].unique()),
        'services': len(df['Service'].unique())
    })

@app.route('/api/sales-by-region')
def sales_by_region():
    region_sales = df.groupby('Region')['Sales'].sum().to_dict()
    return jsonify(region_sales)

@app.route('/api/sales-by-service')
def sales_by_service():
    service_sales = df.groupby('Service')['Sales'].sum().to_dict()
    return jsonify(service_sales)

@app.route('/api/daily-sales')
def daily_sales():
    daily = df.groupby('Date')['Sales'].sum().tail(15).to_dict()
    return jsonify(daily)

@app.route('/api/top-performers')
def top_performers():
    top = df.groupby('Region')['Sales'].sum().nlargest(5).to_dict()
    return jsonify(top)

if __name__ == '__main__':
    print("🚀 Accenture Sales Analytics Dashboard")
    print("📊 Starting server on http://localhost:5000")
    app.run(debug=False, port=5000)