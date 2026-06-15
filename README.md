# 🌱 AgriSense - Smart Crop Planning Advisor

AgriSense is an MLOps-based crop recommendation system that suggests the most suitable crop based on soil nutrients and climatic conditions.

🔗 Live Demo: https://agrisense-8hrx.onrender.com/

Features
- Predicts the best crop using Random Forest Classifier
- 99.32% model accuracy
- MLflow experiment tracking
- Streamlit web interface
- Docker deployment

Input Parameters
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

Tech Stack
- Python
- Scikit-learn
- MLflow
- Streamlit
- Docker

Run Locally
pip install -r requirements.txt
py src/train.py
streamlit run app.py

MLflow Tracking
py -m mlflow ui --backend-store-uri sqlite:///mlflow.db
Open: http://127.0.0.1:5000

Docker
docker build -t agrisense .
docker run -p 8501:8501 agrisense
