from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

@app.route('/seguranca')
def seguranca():
    return render_template('seguranca.html')

if __name__ == '__main__':
    app.run(debug=True)
