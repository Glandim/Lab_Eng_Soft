# Vídeo: https://youtu.be/IZUKYHWK34E

Gabriel Augusto Landim - 1460481821029 	

# Requisitos para executar o projeto:

* Python 3.6 ou superior - [Download](https://www.python.org/downloads/release/python-386/)
* MariaDB - [Download](https://mariadb.com/downloads/)

# Como executar o projeto:

* Clone o projeto:

```
git clone https://github.com/Glandim/Lab_Eng_Soft.git

cd Lab_Eng_Soft

git checkout Segunda-Entrega

git pull
```

* Crie e acesse o Virtual Environment:

```
python -m venv env

cd env\Scripts

activate
```

* Volte a raiz do projeto e instale as dependências:

```
cd ..\..

pip install -r requirements.txt
```

* Crie o arquivo ```.env```:
A um exemplo desse arquivo na raiz da pasta chamado ```.env-exemplo```, esse arquivo é essencial para conexão do projeto ao seu banco de dados, renomeio o arquivo para ```.env``` e siga o exemplo abaixo:
```
MARIA_DATABASE=diseaseBD
MARIA_HOST=127.0.0.1
MARIA_PORT=3306
MARIA_USERNAME=root
MARIA_PASSWORD=123456
```
Utilize nos campos "MARIA_USERNAME" e "MARIA_PASSWORD" seu usuario e senha de administrador do MariaDB.

* Caso essa seja a primeira vez que você esteja executando o projeto, utilize o seguinte comando para inicializar o projeto:
```
python wsgi.py init_db
```
* Após a primeira incicialização utilize o comando a seguir para iniciar a aplicação Flask:
```
python wsgi.py
```
* Após inciar a aplicação irá aparecer a seguinte mensagem, acesse o link para usar a aplicação:
```
* Serving Flask app "src.main" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
