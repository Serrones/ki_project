"""
This is the main script from ki_project. Here, we can set a flask application,
defining services like database, which is not the ki_project's case.

ki_project has just one view, so it was determined this script as its location.

"""


import os
from flask import Flask, render_template

from .api_wrapper.ki_wrapper import get_random_deck


app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , ki_project.py

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)




# Here you find the view for deck randomic requests
@app.route('/')
def get_decks():
    random_deck = get_random_deck()
    return render_template('random_decks.jinja2', random_deck=random_deck)
