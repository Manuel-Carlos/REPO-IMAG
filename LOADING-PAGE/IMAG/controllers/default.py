from IMAG import IMAG
from flask import Flask, render_template,redirect,request,flash,session
import pyrebase


config={
    'apiKey': "AIzaSyAIy3aojg0QbqJLeDUgP5lrDTVjRqbRRrk",
    'authDomain': "meu-imagv-b84d5.firebaseapp.com",
    'databaseURL': "https://meu-imagv-b84d5-default-rtdb.firebaseio.com",
    'projectId': "meu-imagv-b84d5",
    'storageBucket': "meu-imagv-b84d5.appspot.com",
    'messagingSenderId': "319800728840",
    'appId': "1:319800728840:web:5b0e314ac197dbbda3e0bd",
    'measurementId': "G-KH9SQTKGZ1",
    'databaseURL':''
}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
IMAG.secret_key='IMAGSEGURA'
@IMAG.route('/templates/')
@IMAG.route('/')
def home():
    return render_template('index.html')

@IMAG.route('/templates/criar', methods=['POST', 'GET'])
def criar():
    if request.method=='POST':
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("passe")
        try:
            user = auth.create_user_with_email_and_password(email, senha)
            return redirect('/templates/perguntas')
        except:
            return 'falhou na criação da sua conta! Tente de novo'

    return render_template('criar.html')
@IMAG.route('/templates/perguntas')
def pergunta():
    return render_template('perguntas.html')
@IMAG.route('/templates/login', methods=['POST', 'GET'])
def login():
    if ('user' in session):
        return f'online {session["user"]}'
    if request.method == 'POST':
        email=request.form.get('email-lg')
        senha=request.form.get('passe-lg')
        try:
            user = auth.sign_in_with_email_and_password(email, senha)
            session['user']=email
            return redirect('/templates/app-aluno')
        except:
            return 'falhou ao entrar para sua conta! Tente de novo'
    return render_template('login.html')
@IMAG.route('/templates/logout')
@IMAG.route('/templates/app-aluno/logout')
def logout():
    session.pop('user')
    return redirect('/templates/')
@IMAG.route('/templates/app-aluno')
def app_aluno():
    if ('user' in session):
        return render_template('app-aluno.html')
    if not('user' in session):
        return 'precisa-se de fazer o login'


