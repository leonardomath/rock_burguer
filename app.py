from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'hello'

@app.route('/reservar_mesa', methods=['POST'])
def reservar_mesa():
    pass

@app.route('/trabalhe_conosco', methods=['POST'])
def salvar_contato():
    pass

db.create_all()
app.run()