from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

layout = dbc.Container([
    html.H1("Paramètres du Compte", className="text-center mt-4"),
    dbc.Tabs([
        dbc.Tab(label="Informations personnelles", tab_id="informations-personnelles"),
        dbc.Tab(label="Sécurité et connexion", tab_id="securite-connexion"),
        dbc.Tab(label="Préférences utilisateur", tab_id="preferences-utilisateur"),
    ], id="parametres-tabs", active_tab="informations-personnelles"),
    html.Div(id="parametres-content", className="mt-3"),
])

def register_callbacks(app):  # Définition de la fonction register_callbacks
    @app.callback(
        Output("parametres-content", "children"),
        Input("parametres-tabs", "active_tab")
    )
    def render_tab_content(active_tab):
        if active_tab == "informations-personnelles":
            return informations_personnelles_tab()
        elif active_tab == "securite-connexion":
            return securite_connexion_tab()
        elif active_tab == "preferences-utilisateur":
            return preferences_utilisateur_tab()
        return html.P("Contenu non trouvé")

def informations_personnelles_tab():
    return dbc.Card(
        dbc.CardBody([
            html.H4("Informations personnelles", className="card-title"),
            html.P("Ici, vous pouvez modifier vos informations personnelles."),
            # Ajoute ici les champs pour afficher et modifier les informations personnelles
        ])
    )

def securite_connexion_tab():
    return dbc.Card(
        dbc.CardBody([
            html.H4("Sécurité et connexion", className="card-title"),
            html.P("Ici, vous pouvez modifier votre mot de passe."),
            # Ajoute ici les champs pour modifier le mot de passe
        ])
    )

def preferences_utilisateur_tab():
    return dbc.Card(
        dbc.CardBody([
            html.H4("Préférences utilisateur", className="card-title"),
            html.P("Ici, vous pouvez modifier vos préférences utilisateur."),
            dbc.Checklist(
                options=[
                    {"label": "Mode sombre", "value": "sombre"},
                ],
                value=[],
                id="mode-sombre-check",
                switch=True,
            ),
            dcc.Dropdown(
                options=[
                    {"label": "Français", "value": "fr"},
                    {"label": "Anglais", "value": "en"},
                ],
                value="fr",
                id="langue-dropdown",
            ),
        ])
    )