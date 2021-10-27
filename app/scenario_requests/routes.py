from flask import Blueprint, request, render_template, current_app
from flask.templating import render_template

request_app = Blueprint('request', __name__, template_folder='templates')


@request_app.route('/')
def request_menu():
    return render_template('request_menu.html')


@request_app.route('/first-query')
# def first_query():
