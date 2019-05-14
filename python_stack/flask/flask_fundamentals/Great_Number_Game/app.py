"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def index():
    if len(session.keys()) == 0:
        session['counter'] = 0
        session['randomnum'] = 0
    else:
        session['counter'] += 1
    print("Counter", session['counter'])
    import random 	                                # import the random module
    session['randomnum'] = random.randint(1, 100)	# random number between 1-100
    print("Number:", session['randomnum'])
    results = ""
    color = "white"
    return render_template("index.html", results=results, color=color)

@app.route('/results', methods=['POST'])
def results():
    session['number'] = int(request.form['number'])
    if session['number'] == session['randomnum']:
        results = "YOU WIN! it took you " + str(session['counter']) + " tries."
        color = "green"
    elif session['number'] < session['randomnum']:
        results = "Too low! So far " + str(session['counter']) + " tries."
        color = "yellow"
    elif session['number'] > session['randomnum']:
        results = "Too high! it took you " + str(session['counter']) + " tries."
        color = "red"
    print(results)
    return render_template("index.html", results=results, color=color)


@app.route('/reset')
def destroy_session():
    session.clear()
    session['counter'] = 0
    print("Counter", session['counter'])
    import random 	                                # import the random module
    session['randomnum'] = random.randint(1, 100)	# random number between 1-100
    print("Number:", session['randomnum'])
    return redirect("/")

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
