import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Import des pages
from pages import accueil, reclamations, parametres, agent
from components import navbar

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY], suppress_callback_exceptions=True) # Ajout de suppress_callback_exceptions
app.title = "CIRACbot"

# Définition du layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar.Navbar(),  # Utilisation de la barre de navigation
    html.Div(id='page-content', className="container") # Ajout d'un container pour le contenu
])

# Callback pour la navigation
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return accueil.layout
    elif pathname == '/reclamations':
        return reclamations.layout
    elif pathname == '/parametres':
        return parametres.layout
    elif pathname == '/agent':
        return agent.layout
    else:
        return html.Div("Erreur 404 - Page non trouvée")

# Appel des fonctions register_callbacks
accueil.register_callbacks(app)
reclamations.register_callbacks(app)
parametres.register_callbacks(app)
agent.register_callbacks(app)

# Lancement de l'application
if __name__ == '__main__':
    app.run(debug=True)