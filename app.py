from flask import Flask, render_template 

app = Flask("__name__")

@app.route("/")
@app.route("/home")
def home():
    return render_template("/home.html")

@app.route("/contato")
def contato():
    return render_template("/contato.html")

@app.route("/quemSomos")
def quemSomos():
    return render_template("/quemSomos.html")