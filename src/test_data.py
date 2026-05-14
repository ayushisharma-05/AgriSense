import pandas as pd

df = pd.read_csv("data/Crop_recommendation.csv")

print(df.shape)
print(df.head())
print(df["label"].value_counts().head())