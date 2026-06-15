import mlflow
import mlflow.sklearn

def log_experiment(model, accuracy):

    mlflow.set_experiment("AgriSense")

    with mlflow.start_run():

        mlflow.log_param(
            "model_type",
            "RandomForestClassifier"
        )

        mlflow.log_metric(
            "accuracy",
            accuracy
        )

        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="crop_model"
        )

        print("MLflow logging completed successfully")