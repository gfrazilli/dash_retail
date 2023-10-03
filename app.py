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
import dash_bootstrap_components as dbc

# Exposing the Flask Server to enable configuring it for logging in
server = Flask(__name__)

app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.SANDSTONE], server=server, use_pages=True, suppress_callback_exceptions=True
)

# Senhas para testes, trocar isso pela conexão ao bd
VALID_USERNAME_PASSWORD = {"test": "test", "hello": "world"}



# Updating the Flask Server configuration with Secret Key to encrypt the user session cookie
server.config.update(SECRET_KEY=os.getenv("SECRET_KEY"))

class User(UserMixin):
    # User data model. It has to have at least self.id as a minimum
    def __init__(self, username):
        self.id = username


