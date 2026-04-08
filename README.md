#🌍 AQI Prediction using Hybrid ML Framework

#📌 Project Overview

Air pollution has become a major environmental concern.

This project predicts the Air Quality Index (AQI) for selected cities using a Hybrid Machine Learning model trained on historical air pollution data.

The web application allows users to:

Select a city

Fetch its pollution data from the dataset

Predict AQI using trained ML models

View AQI visualization

#🚀 Features

-AQI prediction based on city selection

-Hybrid Machine Learning approach

-Flask-based web application

-Dataset-driven predictions

-Interactive AQI visualization using Matplotlib

#🧠 Machine Learning Models Used
This project combines multiple models to improve prediction accuracy:
-Multiple Linear Regression
-Random Forest Regressor
-Gradient Boosting Regressor
-Stacking Ensemble Model (Hybrid Model)

#🛠️ Tech Stack
Python • Flask • Scikit-learn • Pandas • NumPy • Matplotlib • HTML • CSS

#📂 Project Structure
AQI-Prediction-using-Hybrid-ML-Framework/
│
├── app.py                          # Flask backend
├── Air_quality_prediction.ipynb    # Model training notebook
├── .gitignore
│
├── templates/                      # HTML pages
│   └── index.html
│
├── static/                         # Dataset used by the app
│   └── city_day.csv

#⚙️ How to Run the Project
1️⃣ Clone the repository
   git clone https://github.com/your-username/AQI-Prediction-using-Hybrid-ML-Framework.git
   cd AQI-Prediction-using-Hybrid-ML-Framework

2️⃣ Install dependencies
   pip install -r requirements.txt

3️⃣ Run the Flask app
   python app.py

4️⃣ Open in browser
   http://127.0.0.1:5000/

#📊 Future Improvements
Real-time AQI API integration
More cities & larger dataset
Deploy on cloud (Render/Heroku)
Add deep learning models

#👩‍💻 Author
Suhani Bhoyar
