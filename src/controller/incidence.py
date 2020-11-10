import json

from flask import Blueprint, render_template, request, Response, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from src.controller.Disease import getDiseaseList

from src.model.disease import Disease
from src.model.incidence import Incidence

incidenceBlueprint = Blueprint('incidence', __name__, url_prefix='/incidence')

@incidenceBlueprint.route('/')
def diseaseIndex():
  try:
    diseases = getDiseaseList()
    
  except Exception as error:
    print(error)
    diseases = []

  return render_template('Incidence/incidence.html', title='Cadastro de incidência', data={"diseases": diseases})

@incidenceBlueprint.route('/register', methods=['POST', 'GET'])
def registerIncidence():
  try:
    db = SQLAlchemy(current_app)
    
    obj = request.json

    disease = Disease.query.filter_by(name=obj['disease']).first()
    newIncidence = Incidence(fk_disease=disease.id, date=obj['date'])
    
    with current_app.app_context():
      db.session.add(newIncidence)
      db.session.commit()

    res = json.dumps({'msg': 'A incidência foi cadastrada'})
    return Response(res, mimetype='application/json', status=200)
        
  except SQLAlchemyError as error:
    res = json.dumps({"Erro": str(error.__dict__['orig'])})
    return Response(res, mimetype='application/json', status=500)
  
  except Exception as error:
    res = json.dumps({"Erro": str(error)})
    return Response(res, mimetype='application/json', status=500)
