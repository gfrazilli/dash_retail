import dash
from dash import html, dcc, Output, Input, callback
from flask_login import current_user
from flask import session
#from utils.login_handler import require_login

dash.register_page(__name__)
#require_login(__name__)


def layout():
    if not current_user.is_authenticated:
        return html.Div(["Por favor, faça login  ", dcc.Link("login", href="/login"), " to continue"]) #esse redirecionamento é tão rápido que nem aparece
    

    if not session['permissao'] == 'admin':
        return html.Div(["Acesso não permitido. Apenas o administrador do sistema pode liberar este acesso"]) #esse redirecionamento é tão rápido que nem aparece

    #if permissao errada return acesso não autorizado, fale com adm do sistema para conseguir acesso    

    return html.Div(
        [
            html.H1("Page 2"),
            dcc.RadioItems(
                id="page-2-radios",
                options=[{"label": i, "value": i} for i in ["Orange", "Blue", "Red"]],
                value="Orange",
            ),
            html.Div(id="page-2-content"),
            html.Br(),
            dcc.Link("Go to Page 1", href="/page-1"),
            html.Br(),
            dcc.Link("Go back to home", href="/"),
        ]
    )


@callback(Output("page-2-content", "children"), Input("page-2-radios", "value"))
def page_2_radios(value):
    return f'You have selected "{value}"'