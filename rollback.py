import mlflow
from mlflow import MlflowClient

mlflow.set_tracking_uri("http://127.0.0.1:5000")

client = MlflowClient()

nom_modele = "fraude-tp2"

version = input("Version vers laquelle faire le rollback : ")

client.set_registered_model_alias(
    name=nom_modele,
    alias="production",
    version=version
)

print(
    f"Rollback terminé : version {version} "
    f"est maintenant en production"
)
