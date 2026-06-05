# Sales-Analytics-Dashboard
# 📊 Accenture Sales Analytics Dashboard

A modern, interactive sales analytics dashboard for Accenture company projects. Real-time visualization of sales performance metrics with interactive charts and comprehensive analytics.

## Features

✨ **Key Features:**
- **Real-time Metrics Dashboard** - Total Sales, Orders, Average Sale, Active Regions, Service Lines
- **Interactive Charts**:
  - Sales by Region (Bar Chart)
  - Sales by Service (Doughnut Chart)
  - Daily Sales Trend (Line Chart)
  - Top Performing Regions (Horizontal Bar Chart)
- **Beautiful UI** - Modern gradient design with smooth animations
- **Responsive Design** - Works seamlessly on desktop and tablet devices
- **Fast Performance** - Lightweight and optimized for quick data loading

## Project Structure

```
Sales Analytics Dashboard/
├── mainn.py                 # Flask backend application
├── requirements.txt         # Python dependencies
├── templates/
│   └── index.html          # Main dashboard UI
└── README.md               # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd "c:\Users\DELL\Desktop\Sales Analytics Dashboard"
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python mainn.py
   ```

4. **Access the dashboard:**
   - Open your browser and navigate to: `http://localhost:5000`
   - The dashboard will load with sample sales data

## Usage

Once the application is running:

1. **View Metrics** - The top section displays 5 key performance indicators
2. **Analyze Charts** - Interactive charts update in real-time
3. **Hover Over Charts** - Hover on chart elements to see detailed information
4. **Responsive Layout** - The dashboard adapts to your screen size
   
<img width="1431" height="806" alt="Screenshot 2026-06-05 102035" src="https://github.com/user-attachments/assets/f0edf01e-514e-4bf9-8e83-d0d71a2c266c" />

<img width="1424" height="787" alt="Screenshot 2026-06-05 102053" src="https://github.com/user-attachments/assets/fded70d4-da8e-4317-b9b0-291b5766b023" />

## API Endpoints

The backend provides the following REST API endpoints:

- `GET /` - Main dashboard page
- `GET /api/stats` - Returns summary statistics
- `GET /api/sales-by-region` - Sales breakdown by region
- `GET /api/sales-by-service` - Sales breakdown by service line
- `GET /api/daily-sales` - Daily sales trend (last 15 days)
- `GET /api/top-performers` - Top performing regions

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Charting**: Chart.js (JavaScript charting library)
- **Data Processing**: Pandas (Python data manipulation)
- **Styling**: Custom CSS with gradient backgrounds

## Data

The dashboard uses dynamically generated sample data representing:
- **4 Regions**: North, South, East, West
- **4 Service Lines**: Consulting, Technology, Operations, Security
- **30 Days** of historical sales data
- **Random Sales Values**: $50,000 - $500,000 per transaction

## Customization

### Changing Port
Edit `mainn.py` and modify the port number:
```python
app.run(debug=False, port=8000)  # Change 5000 to your preferred port
```

### Updating Sample Data
Modify the `generate_sales_data()` function in `mainn.py` to customize:
- Date ranges
- Regions
- Service lines
- Sales value ranges

### Styling
Edit the CSS in `templates/index.html` to customize:
- Colors
- Fonts
- Layout
- Animations

## Performance

- **Load Time**: < 2 seconds
- **Data Generation**: Real-time on each request
- **Chart Rendering**: Instant with smooth animations
- **Browser Support**: All modern browsers (Chrome, Firefox, Safari, Edge)

## Troubleshooting

**Port Already in Use:**
```bash
# Change the port in mainn.py or kill the process using port 5000
```

**Dependencies Not Installing:**
```bash
# Try upgrading pip
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Dashboard Not Loading:**
- Ensure Flask is running (check terminal output)
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh browser (Ctrl+Shift+R)

## Development

To modify and test the dashboard:

1. Keep the server running in one terminal
2. Edit files (Python or HTML/CSS)
3. Save changes
4. Refresh browser to see updates (for frontend changes)
5. Restart the server for backend changes (Python)

## Deployment

For production deployment:

1. Replace Flask with a production WSGI server (Gunicorn, uWSGI)
2. Use a reverse proxy (Nginx, Apache)
3. Add SSL/TLS certificates
4. Implement proper error handling and logging
5. Use a real database instead of in-memory data

### Example Gunicorn Deployment:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 mainn:app
```

## License

This project is for Accenture company use.

## Support

For issues or questions about the dashboard, please contact the development team.

## Version History

- **v1.0.0** (June 2026) - Initial release with 4 interactive charts and real-time metrics

---

**Last Updated**: June 5, 2026
