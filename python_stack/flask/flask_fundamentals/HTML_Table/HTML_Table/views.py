"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from HTML_Table import app

@app.route('/')
def lists():
    users = [
       {'first_name' : 'Michael', 'last_name' : 'Choi'},
       {'first_name' : 'John', 'last_name' : 'Supsupin'},
       {'first_name' : 'Mark', 'last_name' : 'Guillen'},
       {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("lists.html", users = users)
