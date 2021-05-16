from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://leonardomath:toor@127.0.0.1/rockburger'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from src import routes