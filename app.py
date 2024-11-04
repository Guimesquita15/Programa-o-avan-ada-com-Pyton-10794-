from flask import Flask, render_template

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/administracao_redes_locais')
def administracao_redes_locais():
    return render_template('administracao_redes_locais.html')

@app.route('/processamento_computacional')
def processamento_computacional():
    return render_template('processamento_computacional.html')

@app.route('/c_e_c++')
def c_e_c():
    return render_template('c e c++.html')

@app.route('/administração_de_bd')
def administração_de_bd():
    return render_template('admin. de base de dados.html')

@app.route('/JAVA')
def JAVA():
    return render_template('prog com java.html')

@app.route('/Python')
def Python():
    return render_template('prog com py.html')

def home():
    return "Olá, Mundo!"

if __name__ == '__main__':
    app.run(debug=True)