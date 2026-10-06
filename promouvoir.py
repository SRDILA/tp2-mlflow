import mlflow
from mlflow import MlflowClient

mlflow.set_tracking_uri("http://127.0.0.1:5000")

client = MlflowClient()

nom_modele = "fraude-tp2"

version = input("Version à promouvoir : ")

client.set_registered_model_alias(
    name=nom_modele,
    alias="staging",
    version=version
)

print(f"Version {version} -> alias staging")

confirmation = input("Promouvoir en production ? (oui/non) : ")

if confirmation.lower() == "oui":
    client.set_registered_model_alias(
        name=nom_modele,
        alias="production",
        version=version
    )

    print(f"Version {version} -> alias production")
else:
    print("Promotion en production annulée")
