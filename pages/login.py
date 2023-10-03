import dash
from dash import html, dcc, Output, Input, callback, no_update
import dash_bootstrap_components as dbc
from app import *

from dash.exceptions import PreventUpdate


dash.register_page(__name__)

class User(UserMixin):
    # User data model. It has to have at least self.id as a minimum
    def __init__(self, username):
        self.id = username

card_style = {
    'width': '300px',
    'min-height':'300px',
    'padding-top': '25px',
    'padding-right': '25px',
    'padding-left': '25px',
    'align-self': 'center'

}



# Login screen
def layout():
    #message = "Ocorreu algum erro durante o login" if "login-state" == 'erro' else '',
    return dbc.Card(
            [
            dcc.Location(id="url_login"),
            html.Legend("Login"),
            dbc.Input(placeholder="Digite seu nome de usuário", type="text", id="user_login", name='username', style={'margin-top': '10px'}),
            dbc.Input(placeholder="Digite sua senha", type="password", id="pwd_login", name='password', style={'margin-top': '10px'}),
            dbc.Button(children="Login", n_clicks=0, type="submit", id="login_button", style={'margin-top': '20px'}),
            html.Div("", id="best"),
            html.Span(title="e",id='mensagem', style ={'text-align': "center"}), #espaço para mensagens de erro
        ],color="secondary", inverse=True, style=card_style#, method='POST'
    )

# #callback de login, migrar para a página de login
@callback(
    [Output('best', 'children'),
     Output('url_login', 'pathname')
     ],

    Input('login_button', 'n_clicks'),

    [State('user_login', 'value'),
     State('pwd_login','value')],
              
              
              )
def login_button_click(n_clicks, username, password):
    if n_clicks == 0:
        raise PreventUpdate
    else:        
        #if VALID_USERNAME_PASSWORD.get(username) is None:
        #    return """invalid username and/or password <a href='/login'>login here</a>"""
        if username == 'test' and password == 'test':
            login_user(User(username))
            session['permissao'] = 'admin' #colocar a permissão do bd
                
            if 'url' in session:
                if session['url']:
                    url = session['url']
                    session['url'] = None
                    return '', url ## redirect to target url
            return '', '/' ## redirect to home
        else:
            session['permissao'] = 'erro_login' #colocar a permissão do bd
            return 'Nome de usuário ou senha incorreta', no_update ## redirect to home
    


# @callback(
#     Output('best', 'children'),
#     Input('login-state', 'data')

#     )
# def mensagem(erro):
#     if erro == "erro":
#         return "Ocorreu algum erro durante o login"
#     else:
#         return ""

