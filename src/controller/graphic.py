from flask import Blueprint, render_template

graphicBlueprint = Blueprint('graphic', __name__, url_prefix='/graphic')

@graphicBlueprint.route('/')
def graphicIndex():
  return render_template('graphic/graphic.html', title='Gráfico das doênças')
