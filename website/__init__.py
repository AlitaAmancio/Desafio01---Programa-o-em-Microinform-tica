from flask import Flask, render_template
from .database import create_contato_table, create_database

def create_app():
    app = Flask(__name__)
    
    from .routes import routes
    app.register_blueprint(routes, url_prefix='/')

    try: create_database()
    except: pass
    try: create_contato_table()
    except: pass

    return app