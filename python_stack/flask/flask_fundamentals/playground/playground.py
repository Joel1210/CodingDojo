from flask import Flask, render_template
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'
@app.route('/play')
def play():
    return render_template("index.html", numtimes=3, bkcolor="blue")
@app.route('/play/<intnum>')
def times(intnum):
    return render_template("index.html", numtimes=int(intnum), bkcolor="blue")
@app.route('/play/<intnum>/<bkcolor>')
def color(intnum, bkcolor):
    return render_template("index.html", numtimes=int(intnum), bkcolor=bkcolor)
if __name__=="__main__":    
    app.run(debug=True)  