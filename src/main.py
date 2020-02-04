from flask import Flask
from flask import request, redirect, url_for
from flask import make_response, render_template
from flask import redirect

app =  Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    return render_template("index.html")

@app.route('/play', methods=['POST'])

numero1 = request.form['numerouno']
numero2 = request.form['numerodos']

suma = numero1 + numero2



if __name__ == '__main__' :
    app.run('0.0.0.0', 5000,debug=True)