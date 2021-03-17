from .app import app, db, render_template
from .models.Visitas import Visitas

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
    visita = Visitas(ip_visita='127.0.0.1', data_visita='2021/11/11')
    db.session.add(visita)
    db.session.commit()
    return '<h1>Visita cadastrada</h1>'