# sales-forecast-dashboard

This project is a sales forecasting dashboard built with Python, using Streamlit and XGBoost.  
It predicts monthly sales based on factors such as advertising spend, weather, temperature, and seasonality.

## Features

- Interactive dashboard to visualize historical sales data
- Sales prediction using machine learning (XGBoost)
- Scenario input for future advertising spend and weather conditions
- Handles seasonality and weekday effects

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Install dependencies with:

```bash
pip install -r requirements.txt


## How to Run
1. Train the model (optional if you already have the model file):
python train_model.py

2.Run the Streamlit app:
streamlit run app.py

3.Access the dashboard at http://localhost:8501


## Data
The sample sales data CSV includes columns for:
Date
Weekday
Month
Advertising Spend (in 10,000 yen units)
Weather conditions (Sunny, Rainy, etc.)
Temperature (°C)
Sales (in 10,000 yen units)
