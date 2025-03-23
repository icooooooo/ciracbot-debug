from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import json
import os
import uuid
from datetime import datetime  # Import du module datetime

DATA_FILE = "reclamations.json"  # Nom du fichier JSON

layout = dbc.Container([
    html.H1("Formulaire de Réclamation", className="text-center mt-4"),
    dbc.Form([
        dbc.Row([
            dbc.Col([
                dbc.Label("Nom et prénom :"),
                dbc.Input(id="reclamation-nom", type="text", placeholder="Votre nom et prénom", className="mb-3"),
            ], md=6),
            dbc.Col([
                dbc.Label("Email :"),
                dbc.Input(id="reclamation-email", type="email", placeholder="Votre email", className="mb-3"),
            ], md=6),
        ]),
        dbc.Label("Description de la Réclamation :"),
        dbc.Textarea(id="reclamation-description", placeholder="Décrivez votre réclamation", className="mb-3"),
        dbc.Button("Soumettre", id="reclamation-submit", color="primary"),
        html.Div(id="reclamation-message", className="mt-3"),
    ]),
])


def register_callbacks(app):
    @app.callback(
        Output("reclamation-message", "children"),
        Input("reclamation-submit", "n_clicks"),
        State("reclamation-nom", "value"),
        State("reclamation-email", "value"),
        State("reclamation-description", "value"),
        prevent_initial_call=True
    )
    def submit_reclamation(n_clicks, nom, email, description):
        if n_clicks is not None and n_clicks > 0:
            if nom and email and description:
                # Obtention de la date et de l'heure actuelles
                now = datetime.now()
                date_heure = now.strftime("%d/%m/%Y %H:%M")  # Formatage de la date et de l'heure

                reclamation = {
                    "id": str(uuid.uuid4()),  # Génération d'un ID unique
                    "nom": nom,
                    "email": email,
                    "description": description,
                    "date": date_heure,  # Ajout de la date et de l'heure
                    "statut": "En attente"  # Ajout du statut par défaut
                }
                try:
                    # Charger les données existantes
                    if os.path.exists(DATA_FILE):
                        with open(DATA_FILE, "r") as f:
                            try:
                                reclamations = json.load(f)
                            except json.JSONDecodeError:
                                reclamations = []
                    else:
                        reclamations = []

                    # Ajouter la nouvelle réclamation
                    reclamations.append(reclamation)

                    # Enregistrer les données
                    with open(DATA_FILE, "w") as f:
                        json.dump(reclamations, f, indent=4)

                    return dbc.Alert("Réclamation soumise avec succès !", color="success")
                except Exception as e:
                    return dbc.Alert(f"Erreur lors de la soumission de la réclamation : {e}", color="danger")
            else:
                return dbc.Alert("Veuillez remplir tous les champs du formulaire.", color="warning")
        return ""