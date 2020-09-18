from flask import Flask

app = Flask(__name__)

@app.route('/')
def Primeira_Entrega():
    return '''
    <h1>
        <p>Sistema de Coleta e Visualização de Dados Epidemiológicos</p>
        <p>Gabriel Augusto Landim - 1460481821029</p>
        <p>Fabricio Galende Marques de Carvalho</p>
    </h1>
    '''

if __name__ == "__main__":
    app.run()