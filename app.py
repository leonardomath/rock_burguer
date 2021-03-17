from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models.Visitas import Visitas

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reservar_mesa', methods=['POST'])
def reservar_mesa():
    pass

@app.route('/trabalhe_conosco', methods=['POST'])
def salvar_contato():
    pass

@app.route('/set_visita', methods=['GET'])
def set_visita():
    visita = Visitas(ip_visita='127.0.0.1', data_visita='23/11/2021')
    db.session.add(visita)
    db.session.commit()
    return '<h1>Visita cadastrada</h1>'

db.create_all()
app.run()