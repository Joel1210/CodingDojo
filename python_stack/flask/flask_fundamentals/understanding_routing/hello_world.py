from flask import Flask
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<mystr>')
def name(mystr):
    return 'Hi ' + mystr + '!'
@app.route('/repeat/<intnum>/<str>')
def strnum(intnum, str):
    temp = str * int(intnum)
    return temp
if __name__=="__main__":    
    app.run(debug=True)    