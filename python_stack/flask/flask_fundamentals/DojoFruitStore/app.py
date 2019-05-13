"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    apple_from_form = request.form['apple']
    blackberry_from_form = request.form['blackberry']
    raspberry_from_form = request.form['raspberry']
    strawberry_from_form = request.form['strawberry']
    first_name_from_form = request.form['first_name']
    last_name_from_form = request.form['last_name']
    student_id_from_form = request.form['student_id']

    return render_template("checkout.html", apple_on_template=apple_from_form, blackberry_on_template=blackberry_from_form, raspberry_on_template=raspberry_from_form, strawberry_on_template=strawberry_from_form, first_name_on_template=first_name_from_form, last_name_on_template=last_name_from_form, student_id_on_template=student_id_from_form)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
