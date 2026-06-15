import pickle
import pandas as pd

# Load trained model
with open("models/model.pkl", "rb") as file:
    model = pickle.load(file)

def predict_crop(features):
    columns = [
        "N",
        "P",
        "K",
        "temperature",
        "humidity",
        "ph",
        "rainfall"
    ]

    input_df = pd.DataFrame([features], columns=columns)

    prediction = model.predict(input_df)[0]

    return prediction