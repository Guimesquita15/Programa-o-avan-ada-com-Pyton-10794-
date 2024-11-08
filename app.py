from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_talisman import Talisman



# Configuração inicial do Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'  # Defina uma chave secreta forte aqui

# Criar um formulário usando Flask-WTF
class MeuFormulario(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Enviar')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'  # Necessário para CSRF

# Configura o Talisman com uma Content Security Policy (CSP) personalizada
csp = {
    'default-src': "'self'",
    'script-src': ["'self'", 'https://trusted-cdn.com'],
    'style-src': "'self' https://trusted-styles.com",
    'img-src': "'self' data:",
    'object-src': "'none'"
}
talisman = Talisman(app, content_security_policy=csp)

# Criar classe do formulário
class FormSeguranca(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Enviar')

# Rota para a página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rotas para os conteúdos
@app.route('/content1')
def content1():
    return render_template('content1.html')

@app.route('/content2')
def content2():
    return render_template('content2.html')

@app.route('/content3')
def content3():
    return render_template('content3.html')

@app.route('/content4')
def content4():
    return render_template('content4.html')

@app.route('/content5')
def content5():
    return render_template('content5.html')

@app.route('/content6')
def content6():
    return render_template('content6.html')

# Rota para módulos
@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

# Rota para a página de segurança
@app.route('/seguranca', methods=['GET', 'POST'])
def seguranca():
    form = MeuFormulario()
    if form.validate_on_submit():  # Verifica se o formulário foi submetido e validado
        nome = form.nome.data
        flash(f"Formulário enviado com sucesso por {nome}!", "success")
        # Não redirecionamos, apenas renderizamos novamente a página com a mensagem de sucesso
    elif form.is_submitted() and not form.validate():  # Se o formulário foi submetido mas não validado
        flash("Erro: Formulário não validado. Verifique os campos e tente novamente.", "error")
    # Renderizamos a página com o modal e as mensagens flash (se houver)
    return render_template('seguranca.html', form=form)

# Função para adicionar headers de segurança adicionais
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