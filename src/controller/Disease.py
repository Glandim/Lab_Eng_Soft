import json

from flask import Blueprint, render_template, request, Response, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from src.model.disease import Disease

diseaseBlueprint = Blueprint('disease', __name__, url_prefix='/disease')

@diseaseBlueprint.route('/')
def diseaseIndex():
  return render_template('Disease/disease.html', title='Cadastro de doênças')

@diseaseBlueprint.route('/register', methods=['POST'])
def save():
  db = SQLAlchemy(current_app)

  obj = request.json

  newDisease = Disease(**obj)

  with current_app.app_context():
    db.session.add(newDisease)
    db.session.commit()

  res = json.dumps({'msg': 'Doênça cadastrada com sucesso!'})
  return Response(res, mimetype='application/json', status=200)

def getDiseaseList():
  try:
    db = SQLAlchemy(current_app)

    disease = Disease.query.all()
    if not disease:
      raise "Nenhuma doênça cadastrada!"

    disease = list(map(lambda x: x.name, disease))

    return disease

  except SQLAlchemyError as error:
    res = json.dumps({"Erro": str(error.__dict__['orig'])})
    print(res)
    raise None
  
  except Exception as error:
    res = json.dumps({"Erro": str(error)})
    print(res)
    raise None
