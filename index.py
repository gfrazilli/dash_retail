"""
 CREDIT: This code was originally adapted for Pages  based on Nader Elshehabi's  article:
   https://dev.to/naderelshehabi/securing-plotly-dash-using-flask-login-4ia2
   https://github.com/naderelshehabi/dash-flask-login

   This version is updated by Dash community member @jinnyzor For more info see:
   https://community.plotly.com/t/dash-app-pages-with-flask-login-flow-using-flask/69507

For other Authentication options see:
  Dash Enterprise:  https://dash.plotly.com/authentication#dash-enterprise-auth
  Dash Basic Auth:  https://dash.plotly.com/authentication#basic-auth

"""


import os
from flask import Flask, request, redirect, session
from flask_login import login_user, LoginManager, UserMixin, logout_user, current_user

import dash
from dash import dcc, html, Input, Output, State, ALL
from dash.exceptions import PreventUpdate
from utils.login_handler import restricted_page

from app import *

# #callback de login, migrar para a página de login
# @server.route('/login', methods=['POST'])
# def login_button_click():
#     if request.form:
#         username = request.form['username']
#         password = request.form['password']
#         if VALID_USERNAME_PASSWORD.get(username) is None:
#             return """invalid username and/or password <a href='/login'>login here</a>"""
#         if VALID_USERNAME_PASSWORD.get(username) == password:
#             login_user(User(username))
#             session['permissao'] = 'admin2' #colocar a permissão do bd
            
#             if 'url' in session:
#                 if session['url']:
#                     url = session['url']
#                     session['url'] = None
#                     return redirect(url) ## redirect to target url
#             return redirect('/') ## redirect to home
#         return """invalid username and/or password <a href='/login'>login here</a>"""


# Login manager object will be used to login / logout users
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = "/login"


@login_manager.user_loader
def load_user(username):
    """This function loads the user by user id. Typically this looks up the user from a user database.
    We won't be registering or looking up users in this example, since we'll just login using LDAP server.
    So we'll simply return a User object with the passed in username.
    """
    return User(username)


app.layout = html.Div(
    [
        dcc.Location(id="url"),
        html.Div(id="user-status-header"),
        html.Hr(),
        dcc.Store(id='login-state', data=""), #guardar como está o login(Store guarda informação JSON no Browser)
        html.Div(dash.page_container, style ={'height': '100vh', 'display':'flex', 'justify-content': 'center'}),
        #dash.page_container, 
    ]
)


@app.callback(
    Output("user-status-header", "children"), #primeira div é o header com botão login/logout, segunda é a página em si que está sendo acessada.
    Output('url','pathname'),
    Input("url", "pathname"),
    Input({'index': ALL, 'type':'redirect'}, 'n_intervals')
)
def update_authentication_status(path, n):
    ### logout redirect
    if n:
        if not n[0]:
            return '', dash.no_update
        else:
            return '', '/login'

    
    ### if path login and logout hide links
    if path in ['/login', '/logout']:
        return '', dash.no_update
    
    ### testa se usuário está autenticado para criar botão de login/logout no topo
    if current_user.is_authenticated:
        if path == '/login':
            return dcc.Link("logout", href="/logout"), '/' #se tentar entrar na página de login com user autenticado, redireciona para home "/"
        return dcc.Link("logout", href="/logout"), dash.no_update #header com botão logout
    else:
        return dcc.Link("login", href="/login"), dash.no_update



if __name__ == "__main__":
    app.run_server(debug=True, port='8051')