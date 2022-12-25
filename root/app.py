import webview
from flask import Flask, render_template
from src import views, api
from settings import flask_config, window_config

server = Flask(__name__, **flask_config)
api = api.Evaluation()

server.register_blueprint(views.routes)

webview.create_window('Broken Calc v2', server, js_api=api, **window_config)
webview.start(debug=True)