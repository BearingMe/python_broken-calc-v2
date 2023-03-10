from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    try:
        return render_template('index.html')

    except TemplateNotFound:
        abort(404)