import mlflow
import pandas as pd

mlflow.set_tracking_uri("http://127.0.0.1:5000")

modele = mlflow.pyfunc.load_model(
    "models:/fraude-tp2@production"
)

X = pd.DataFrame([
    {
        "montant": 5000.0,
        "anciennete": 10,
        "freq_24h": 8,
        "nuit": 1
    }
])

prediction = modele.predict(X)

print("Données :")
print(X)

print("\nPrédiction :", prediction)
