from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('pagina principal.html')

@app.route('/Justificacion')
def justificacion():
    return render_template('justificacion.html')

@app.route('/crisisdeextincion')
def crisisdeextincion():
    return render_template('crisis de extincion.html')

@app.route('/reciclaje')
def reciclaje():
    return render_template('reciclaje.html')

@app.route('/tips')
def tips():
    return render_template('tips para ayudar.html')