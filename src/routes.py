import socket
from datetime import datetime
import bcrypt
from flask import make_response, request, url_for, send_from_directory, session
from flask.signals import message_flashed
from werkzeug.datastructures import ViewItems
from werkzeug.utils import redirect
import os
from bcrypt import _bcrypt, hashpw

from .app import app, db, render_template
from .models.Visitas import Visitas
from .models.Mensagens import Mensagens
from .models.Lanches import Lanches
from .models.Usuarios import Usuarios

@app.route('/')
def index():
    site_visitado = request.cookies.get('site_visitado')
    lanches = Lanches.query.all()

    if not site_visitado:
        data = datetime.now()
        data_visita = data.strftime('%Y/%m/%d')
        ip_visita = socket.gethostbyname(socket.gethostname())
        visita = Visitas(ip_visita=ip_visita, data_visita=data_visita)
        db.session.add(visita)
        db.session.commit()

        res = make_response(render_template('index.html', lanches=lanches))
        res.set_cookie('site_visitado', 'sim')
        return res

    return render_template('index.html', lanches=lanches)

@app.route('/dashboard/login', methods=['GET', 'POST'])
def dashboard_login():
    salt = '$2b$12$kPWOwySXS2mkPStuMCGKS.'
    if request.form:
        usuario = request.form['usuario']
        senha = request.form['senha']

        if not usuario or not senha:
            raise Exception('Preencher todos os campos')

        usuario = Usuarios.query.filter_by(usuario=usuario).first()

        if not bcrypt.checkpw(senha.encode('utf-8'), usuario.senha.encode('utf-8')):
            raise Exception('Usúario ou senha errada')

        session['usuario_logado'] = usuario.usuario

        return redirect(url_for('dashboard'))

    return render_template('dashboard_login.html')
    
@app.route('/dashboard')
def dashboard():
    if not 'usuario_logado' in session:
        return redirect(url_for('dashboard_login'))

    visitas = Visitas.query.count()
    lanches = Lanches.query.all()

    return render_template('dashboard.html', visitas=visitas, lanches=lanches, dashboard=True)

@app.route('/dashboard/mensagens')
def mensagens():
    mensagens = Mensagens.query.all()
    visitas = Visitas.query.count()

    return render_template('mensagens.html', mensagens=mensagens, visitas=visitas, mensagem=True)

@app.route('/contato')
def contato():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']

    if not nome or not email or not mensagem:
        raise Exception('Preencher todos os campos')

    mensagem = Mensagens(nome_contato=nome, email_contato=email,
                         mensagem=mensagem)
    
    return redirect(url_for('index'))

@app.route('/dashboard/novo_produto', methods=['POST'])
def novo_produto():
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    foto = request.files['foto']

    if not foto:
        raise Exception('Envie uma foto')

    foto_nome = foto.filename

    foto.save(os.path.join('src/uploads', foto_nome))

    produto = Lanches(titulo=titulo, descricao=descricao, 
                       foto=foto_nome)

    db.session.add(produto)
    db.session.commit()

    # raise Exception(titulo, descricao, foto_nome)
    return redirect(url_for('dashboard'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # raise Exception('heres')
    return send_from_directory('uploads', filename)

@app.route('/dashboard/remover/<id_lanche>', methods=['GET'])
def remover_lanche(id_lanche):
    if not id_lanche:
        raise Exception('Lanche não existe.')
    # raise Exception(id_lanche)
    lanche = Lanches.query.filter_by(id_lanche=id_lanche).first()

    db.session.delete(lanche)
    db.session.commit()

    return redirect(url_for('dashboard'))

@app.route('/dashboard/sair')
def sair():
    session.pop('usuario_logado', None)
    return redirect(url_for('dashboard_login'))

@app.route('/nova_mensagem', methods=['POST'])
def nova_mensagem():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']

    if not nome or not email or not mensagem:
        raise Exception('Preencher todos os campos')

    mensagem = Mensagens(nome_contato=nome, email_contato=email, mensagem=mensagem)

    db.session.add(mensagem)
    db.session.commit()

    return redirect(url_for('index'))