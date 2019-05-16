from datetime import datetime
from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'none of your business' # set a secret key for security purposes

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
@app.route('/users')
def users():
    if len(session.keys()) == 0:
        session['user_id'] = 0
    mysql = connectToMySQL('mydb')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    return render_template("users.html", title="All Users", users=users)

@app.route('/users/getid', methods=['POST'])
def newuser():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
        }
    mysql = connectToMySQL('mydb')
    user_id = mysql.query_db(query, data)
    session['user_id'] = user_id
    path = "/users/" + str(user_id) + "/user"
    return redirect(path)

@app.route('/users/<user_id>/user')
def showuser(user_id):
    mysql = connectToMySQL('mydb')
    query = "SELECT * FROM users WHERE user_id=" + str(user_id) + ";"
    user = mysql.query_db(query)
    first_name=user[0]['first_name']
    last_name=user[0]['last_name']
    email=user[0]['email']
    created_at=user[0]['created_at']
    updated_at=user[0]['updated_at']
    return render_template('user.html', title="Show User", user_id=user_id, first_name=first_name, last_name=last_name, email=email, created_at=created_at, updated_at=updated_at)

@app.route('/users/<user_id>/delete')
def deleteuser(user_id):
    mysql = connectToMySQL('mydb')
    query = "DELETE FROM users WHERE user_id=" + str(user_id) + ";"
    user = mysql.query_db(query)
    return redirect('/users')

@app.route('/users/<user_id>/update', methods=['POST'])
def updateuser(user_id):
    mysql = connectToMySQL('mydb')
    query = "UPDATE users SET first_name = '" + str(request.form['first_name']) + "', last_name = '" + str(request.form['last_name']) + "', email = '" + str(request.form['email']) + "', updated_at = NOW() WHERE user_id=" + str(user_id) + ";"
    mysql.query_db(query)
    session['user_id'] = user_id
    path = "/users/" + str(user_id) + "/user"
    return redirect(path)

@app.route('/users/new')
def new():   
    return render_template('new.html', title="New User")

@app.route('/users/<user_id>/edit')
def edituser(user_id):
    mysql = connectToMySQL('mydb')
    query = "SELECT * FROM users WHERE user_id=" + str(user_id) + ";"
    user = mysql.query_db(query)
    first_name=user[0]['first_name']
    last_name=user[0]['last_name']
    email=user[0]['email']
    return render_template('edit.html', title="Edit User", user_id=user_id, f_name=first_name, l_name=last_name, em=email)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
