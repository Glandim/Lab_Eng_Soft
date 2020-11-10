import os

from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy

from src.controller.Disease import diseaseBlueprint
from src.controller.incidence import incidenceBlueprint
from src.controller.graphic import graphicBlueprint
from src.controller.table import tableBlueprint

from src.model.disease import db as diseaseDb
from src.model.incidence import db as incidenceDb

load_dotenv(find_dotenv())

template_dir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'src')
template_dir = os.path.join(template_dir, 'view')

app = Flask(__name__, template_folder=template_dir, static_folder=template_dir )

_USERNAME = os.getenv('MARIA_USERNAME')
_PASSWORD = os.getenv('MARIA_PASSWORD')
_DATABASE = os.getenv('MARIA_DATABASE')
_HOST = os.getenv('MARIA_HOST')
_PORT = os.getenv('MARIA_PORT')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{_USERNAME}:{_PASSWORD}@{_HOST}:{_PORT}/{_DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

diseaseDb.init_app(app)
incidenceDb.init_app(app)

app.register_blueprint(diseaseBlueprint)
app.register_blueprint(incidenceBlueprint)
app.register_blueprint(graphicBlueprint)
app.register_blueprint(tableBlueprint)

def init_db(appFlask):
    db = SQLAlchemy(appFlask)
    engine = db.create_engine(f'mysql+pymysql://{_USERNAME}:{_PASSWORD}@{_HOST}:{_PORT}', {})
    try:
        engine.execute(f"CREATE DATABASE {_DATABASE}") 
    except Exception as error:
        print(error)
        pass
    
    with appFlask.app_context():
        diseaseDb.create_all()
        incidenceDb.create_all()

@app.route('/')

def home():
    return render_template('Home/home.html', title='Home')
