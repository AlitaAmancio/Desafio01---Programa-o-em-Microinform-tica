from flask import render_template, Blueprint, request, url_for
from .database import insert_data, find_data

routes = Blueprint('routes', __name__)

@routes.route("/")
@routes.route("/home")
def home():
    return render_template("/home.html", title="Home")

@routes.route("/quemSomos")
def quemSomos():
    return render_template("/quemSomos.html", title="Quem Somos")

@routes.route("/mensagens")
def info():
    info = find_data()
    if len(info) > 0:
        return render_template("mensagens.html", info = find_data(), title="Mensagens")
    else: 
        return render_template("mensagens.html", title="Mensagens")

@routes.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        email = request.form.get("email")
        assunto = request.form.get("assunto")
        descricao = request.form.get("descricao")
        insert_data(email, assunto, descricao)
        return render_template("/contato.html", title= "Contato", msg="Sucesso!")
    
    return render_template("/contato.html", title="Contato")
