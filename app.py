from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)
# Configura o Talisman com uma Content Security Policy (CSP) personalizada
csp = {
    'default-src': "'self'",
    'script-src': ["'self'", 'https://trusted-cdn.com'],
    'style-src': "'self' https://trusted-styles.com",
    'img-src': "'self' data:",
    'object-src': "'none'"
}
talisman = Talisman(app, content_security_policy=csp)

# Rota para a página principal
@app.route('/')
def home():
    return render_template('index.html')

# Rota para módulos
@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

# Rota para a página de segurança
@app.route('/seguranca')
def seguranca():
    return render_template('seguranca.html')

# Função para adicionar headers de segurança adicionais (se necessário)
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# Executa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
