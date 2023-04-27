from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort


app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Twoją przeglądarką jest {}</p>'.format(user_agent)


@app.route('/user/<name>')
def user(name):
    return '<h1>Witaj, {}!</h1>'.format(name)

@app.route('/b')
def b():
    return '<h1>Nieprawidłowe żądanie</h1>', 400

@app.route('/o')
def o():
    response = make_response('<h1>Ten dokument zawiera plik cookie!</h1>')
    response.set_cookie('odpowiedź', '42')
    return response

@app.route('/p')
def p():
    return redirect('http://www.przyklad.com')


@app.route('/u/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Witaj, {}</h1>'.format(user.name)
    
    
    
