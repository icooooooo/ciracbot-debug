import dash_bootstrap_components as dbc
from dash import html, dcc

def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Accueil", href="/")),
            dbc.NavItem(dbc.NavLink("Réclamations", href="/reclamations")),
            dbc.NavItem(dbc.NavLink("Paramètres", href="/parametres")),
            dbc.NavItem(dbc.NavLink("Agent", href="/agent")),
        ],
        brand="CIRACbot",
        brand_href="/",
        color="primary",
        dark=True,
    )
    return navbar