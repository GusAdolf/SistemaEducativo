#IMPORTAR LIBRERIA PARA USAR FRAMEWORK FLASK
from flask import Flask
from flask import render_template
import os
from flask import request
import backend
##llamado a flask
app = Flask(__name__)

##servicio web
@app.route('/', methods = ["GET","POST"])
def home():
    return render_template('index.html')

@app.route('/cursos', methods = ["GET","POST"])
def cursos():
    return render_template('cursos.html')

@app.route('/login', methods = ["GET","POST"])
def login():
    return render_template('login.html')




##ejecutar el servicio web
if __name__=='__main__':
    #OJO QUITAR EL DEBUG EN PRODUCCION
    app.run(host='0.0.0.0', port=5000, debug=True)