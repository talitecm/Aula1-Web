from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #para rodar: flask run --debug
def inicio():
    return render_template('inicio.html')

@app.route('/formulario') #para rodar: flask run --debug
def formulario():
    return render_template('formulario.html')