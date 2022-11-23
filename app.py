from flask import Flask, render_template 

app = Flask("__name__")

@app.route("/")
@app.route("/home")
def home():
    return render_template("/home.html", title="Home")

@app.route("/contato")
def contato():
    return render_template("/contato.html", title="Contato")

@app.route("/quemSomos")
def quemSomos():
    return render_template("/quemSomos.html", title="Quem Somos")