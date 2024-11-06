from flask import Flask, render_template

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

<<<<<<< HEAD
@app.route('/seguranca')
def seguranca():
    return render_template('seguranca.html')
=======
def home():
    return "Olá, Mundo!"
>>>>>>> 4265f87f1d77108e4f921c06f761da918ec6583a

if __name__ == '__main__':
    app.run(debug=True)




