"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def root():
    return render_template("index.html", firstcolor="red", secondcolor="black")
@app.route('/<firstcolor>/<secondcolor>')
def checkerboard(firstcolor, secondcolor):
    return render_template("index.html", firstcolor=firstcolor, secondcolor=secondcolor)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)