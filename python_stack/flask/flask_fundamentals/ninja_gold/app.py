"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'none of your business' # set a secret key for security purposes

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
import random

@app.route('/')
def index():
    if len(session.keys()) == 0:
        session['gold'] = 0
        session['activity'] = []
    gold = 0
    color = "default"
    return render_template("index.html", gold=0, color="default", activities=session['activity'])

@app.route('/process_money', methods=['POST', 'GET'])
def process_money():
    gold = session['gold']
    if request.form['building'] == 'farm':
        color = "primary"
        session['randomnum'] = random.randint(10, 20)
        session['gold'] += session['randomnum']
        activity = print("Gained {:d} gold!!".format(session['randomnum']))
        session['activity'].insert(0, {'color' : 'success', 'action' : 'Gained ' + str(session['randomnum']) + 'gold!!'})
    if request.form['building'] == 'cave':
        color = "primary"
        session['randomnum'] = random.randint(5, 10)
        session['gold'] += session['randomnum']
        activity = print("Gained {:d} gold!!".format(session['randomnum']))
        session['activity'].insert(0, {'color' : 'success', 'action' : 'Gained ' + str(session['randomnum']) + 'gold!!'})
    if request.form['building'] == 'house':
        color = "primary"
        session['randomnum'] = random.randint(2, 5)        
        session['gold'] += session['randomnum']
        activity = print("Gained {:d} gold!!".format(session['randomnum']))
        session['activity'].insert(0, {'color' : 'success', 'action' : 'Gained ' + str(session['randomnum']) + 'gold!!'})
    if request.form['building'] == 'casino':
        session['randomnum'] = random.randint(-50, 50)
        session['gold'] += session['randomnum']
        if session['randomnum'] < 0:
            color = "danger"
            activity = print("Lost {:d} gold!!".format(session['randomnum']))
            session['activity'].insert(0, {'color' : color, 'action' : 'Lost ' + str(session['randomnum']) + 'gold!!'})
        else:
            color = "primary"
            activity = print("Gained {:d} gold!!".format(session['randomnum']))
            session['activity'].insert(0, {'color' : 'success', 'action' : 'Gained ' + str(session['randomnum']) + 'gold!!'})
        gold = session['gold']
    return render_template("index.html", gold=gold, color=color, activities=session['activity'])

@app.route('/reset')
def destroy_session():
    session.clear()
    if len(session.keys()) == 0:
        session['gold'] = 0
        session['activity'] = []
    gold = session['gold']
    return redirect("/")

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
