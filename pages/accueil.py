from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

layout = dbc.Container([
    html.H1("Bienvenue sur CIRACbot", className="text-center mt-4"),
    html.P("Votre assistant bancaire intelligent", className="text-center"),

    # Chatbot Section
    dbc.Row([
        dbc.Col([
            dbc.Form([
                html.Div(id="chatbot-container", children=[  # Le composant est créé ici
                    html.Div("👋 Bonjour ! Comment puis-je vous aider ?", className="chatbot-message"),
                ], className="chatbot-box"),
                dcc.Input(id="user-input", type="text", placeholder="Écrivez votre message...", className="chatbot-input"),
                dbc.Button("Envoyer", id="send-btn", color="primary", className="mt-2")
            ]),
        ], width=6)
    ], justify="center"),
])

def register_callbacks(app):
    @app.callback(
        Output("chatbot-container", "children"),
        Input("send-btn", "n_clicks"),
        State("user-input", "value"),
        prevent_initial_call=True
    )
    def update_chat(n_clicks, user_input):
        if n_clicks is not None and n_clicks > 0:
            # Ajoute les messages précédents et le nouveau message à la liste
            nouveau_message = html.Div([
                html.Div(f"Vous: {user_input}", className="user-message"),
                html.Div("🤖 CIRACbot : Je suis en développement!", className="chatbot-message")
            ])
            return nouveau_message
        return ""