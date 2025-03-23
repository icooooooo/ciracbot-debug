from dash import html, dcc, Input, Output, State, ALL
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import dash
import json
import os
import operator
from datetime import datetime

DATA_FILE = "reclamations.json"  # Nom du fichier JSON
DEFAULT_SORT_COLUMN = "date"  # Colonne de tri par défaut
DEFAULT_SORT_DIRECTION = False  # False = Descendant, True = Ascendant

layout = dbc.Container([
    html.H1("Interface Agent", className="text-center mt-4"),
    dbc.Tabs([
        dbc.Tab(label="Suivi des réclamations", tab_id="suivi-reclamations"),
    ], id="agent-tabs", active_tab="suivi-reclamations"),
    html.Div(id="agent-content", className="mt-3"),
    dcc.Store(id="sort-state", data={"column": DEFAULT_SORT_COLUMN, "direction": DEFAULT_SORT_DIRECTION}),
])

def register_callbacks(app):
    @app.callback(
        Output("agent-content", "children"),
        Input("agent-tabs", "active_tab"),
        Input("sort-state", "data"),
    )
    def render_tab_content(active_tab, sort_state):
        if active_tab == "suivi-reclamations":
            sort_column = sort_state["column"]
            sort_direction = sort_state["direction"]

            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as f:
                    try:
                        reclamations = json.load(f)
                    except json.JSONDecodeError:
                        reclamations = []
            else:
                reclamations = []

            reclamations.sort(key=lambda r: datetime.strptime(r.get("date", "01/01/1900 00:00"), "%d/%m/%Y %H:%M"), reverse=sort_direction)

            table = dbc.Table([
                html.Thead(html.Tr([
                    html.Th(html.Button("Nom", id="sort-nom")),
                    html.Th(html.Button("Date", id="sort-date")),
                    html.Th(html.Button("Statut", id="sort-statut")),
                ]))
            ] + [
                html.Tbody([
                    html.Tr([
                        html.Td(r["nom"]),
                        html.Td(r["date"]),
                        html.Td(r["statut"]),
                    ]) for r in reclamations
                ])
            ], bordered=True, striped=True, hover=True)

            return dbc.Card(dbc.CardBody([html.H4("Suivi des réclamations"), table]))
        return html.P("Contenu non trouvé")

    @app.callback(
        Output("sort-state", "data"),
        Input("sort-nom", "n_clicks"),
        Input("sort-date", "n_clicks"),
        Input("sort-statut", "n_clicks"),
        State("sort-state", "data")
    )
    def sort_table(n_clicks_nom, n_clicks_date, n_clicks_statut, sort_state):
        ctx = dash.callback_context
        if not ctx.triggered:
            raise PreventUpdate

        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
        column = trigger_id.split("-")[1]
        direction = not sort_state["direction"] if column == sort_state["column"] else False
        return {"column": column, "direction": direction}