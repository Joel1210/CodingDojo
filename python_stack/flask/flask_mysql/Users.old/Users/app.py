from datetime import datetime
from flask import Flask, render_template, request, redirect, session
from Users import app
from mySQLconnection import connectToMySQL  
app.secret_key = 'none of your business' # set a secret key for security purposes

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def index():
    if len(session.keys()) == 0:
        session['user_id'] = 0
    mysql = connectToMySQL('my_db')
    friends = mysql.query_db('SELECT * FROM users;')
    print(friends)
    render_template('index.html')

@app.route('/users/getid', method='POST')
def showuser():

    render_template('user.html')

@app.route('/users/<user_id>/delete', method='GET')
def delete(user_id):
    render_template('index.html')

@app.route('/users/new', method='POST')
def new():
    render_template('new.html')

@app.route('/users/<user_id>/edit', method='GET')
def edit(user_id):
    render_template('edit.html', user_id)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)