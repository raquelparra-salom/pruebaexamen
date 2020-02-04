from flask import Flask
from flask import request, redirect, url_for
from flask import make_response, render_template
from flask import redirect

app =  Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    return render_template("index.html")

@app.route('/play', methods=['POST'])
def play():

numerouno = request.form['numerouno']
numerodos = request.form['numerodos']

suma = int(numerouno) + int(numerodos)
    return render_template("play.html")
    return render_template("play.html", suma=suma)



if __name__ == '__main__' :
    app.run('0.0.0.0', 5000,debug=True)