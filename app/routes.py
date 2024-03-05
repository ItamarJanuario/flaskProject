from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    #passando parametros para uma pagina html

    nome = 'ITAMAR'
    dados = {
        'profissao': 'Professora',
        'CRM': '2131233'
    }
    return render_template("index.html", nome = nome,
                            dados  = dados)



@app.route('/contato')
def contato():
    return render_template('contato.html')