"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

## Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app


@app.route('/')
def index():
    if len(session.keys()) == 0:
        session['counter']= 0
    else:
        session['counter'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    session['counter'] = 0
    return redirect("/")

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
