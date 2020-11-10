from flask import Blueprint, render_template

tableBlueprint = Blueprint('table', __name__, url_prefix='/table')

@tableBlueprint.route('/')
def tableIndex():
  return render_template('table/table.html', title='Tabela das incidências')
  