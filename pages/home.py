import dash
from dash import html, dcc

dash.register_page(__name__, path="/")
#home pós_login


layout = html.Div(
    [
        html.H1("Bem vindo a Frazilli"),
        dcc.Link("Go to Page 1", href="/page-1"),
        html.Br(),
        dcc.Link("Go to Page 2", href="/page-2"),
        html.Br(),
        dcc.Link("Go to Page 3", href="/page-3"),
    ]
)
