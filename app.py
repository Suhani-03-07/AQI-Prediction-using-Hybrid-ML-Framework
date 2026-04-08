import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
import time

app = Flask(__name__)

# ✅ Load ONLY stack model
stack_model = pickle.load(open("stack_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    city = data['city']

    df = pd.read_csv("static/city_day.csv")
    df.columns = df.columns.str.strip()

    pollutants = ['PM2.5','PM10','NO2','CO','SO2','O3']
    df[pollutants] = df[pollutants].fillna(df[pollutants].mean())

    city_data = df[df['City'] == city]

    if city_data.empty:
        return jsonify({'error': 'City not found'})

    avg = city_data.mean(numeric_only=True)

    features = np.array([[ 
        avg['PM2.5'], avg['PM10'], avg['NO2'],
        avg['CO'], avg['SO2'], avg['O3']
    ]])

    # ✅ Meta model prediction
    final_pred = stack_model.predict(features)[0]

    # ===== FUTURE PREDICTION =====
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    city_data = df[df['City'] == city].copy()
    city_data['Year'] = city_data['Date'].dt.year

    yearly_data = city_data.groupby('Year').mean(numeric_only=True)
    last_year_data = yearly_data.iloc[-1]

    future_years = [2021, 2022, 2023, 2024, 2025]
    future_predictions = []

    current_features = np.array([[ 
        last_year_data['PM2.5'], last_year_data['PM10'], last_year_data['NO2'],
        last_year_data['CO'], last_year_data['SO2'], last_year_data['O3']
    ]])

    for year in future_years:
        pred = stack_model.predict(current_features)[0]
        future_predictions.append(pred)

        current_features = current_features * 1.02  # simulate trend

    # ===== GRAPH =====
    plt.figure(figsize=(6,4))
    plt.figure(figsize=(6,4))

# Convert years to int (just to be safe)
    future_years = list(map(int, future_years))

    plt.plot(future_years, future_predictions, marker='o')

# ✅ Force only integer ticks (fixes 2021.5 issue)
    plt.xticks(future_years)

    plt.title(f"Future AQI Prediction (2021–2025) - {city}")
    plt.xlabel("Year")
    plt.ylabel("Predicted AQI")
    plt.grid(True)
    plt.title(f"Future AQI Prediction (2021–2025) - {city}")
    plt.xlabel("Year")
    plt.ylabel("Predicted AQI")
    plt.grid(True)

    graph_path = "static/aqi_graph.png"
    plt.savefig(graph_path, bbox_inches='tight')
    plt.close()

    graph_url = f"/static/aqi_graph.png?t={int(time.time())}"

    return jsonify({
        'aqi': round(final_pred, 2),
        'graph': graph_url
    })

if __name__ == "__main__":
    app.run(debug=True)