import dash
from dash import html, dcc
from flask_login import logout_user, current_user
from flask import session

dash.register_page(__name__)


def layout():
    if current_user.is_authenticated:
        logout_user()
        session['permissao'] = '' #colocar a permissão do bd
    return html.Div(
        [
            html.Div(html.H2("Você saiu do sistema e será redirecionado para a página inicial.")),
            dcc.Interval(id={'index':'redirectLogin', 'type':'redirect'}, n_intervals=0, interval=1*3000)
        ]
    )