from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///secrets.db'  # Usando SQLite para simplicidade
db = SQLAlchemy(app)

class Ambiente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    aplicacoes = db.relationship('Aplicacao', backref='ambiente', lazy=True)

class Aplicacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    ambiente_id = db.Column(db.Integer, db.ForeignKey('ambiente.id'), nullable=False)
    segredos = db.relationship('Segredo', backref='aplicacao', lazy=True)

class Segredo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chave = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.String(100), nullable=False)
    aplicacao_id = db.Column(db.Integer, db.ForeignKey('aplicacao.id'), nullable=False)

@app.route('/criar_ambiente', methods=['POST'])
def criar_ambiente():
    dados = request.json
    novo_ambiente = Ambiente(nome=dados['nome'])
    db.session.add(novo_ambiente)
    db.session.commit()
    return jsonify({'mensagem': 'Ambiente criado com sucesso!'})

@app.route('/criar_aplicacao', methods=['POST'])
def criar_aplicacao():
    dados = request.json
    ambiente_id = dados['ambiente_id']
    novo_aplicacao = Aplicacao(nome=dados['nome'], ambiente_id=ambiente_id)
    db.session.add(novo_aplicacao)
    db.session.commit()
    return jsonify({'mensagem': 'Aplicação criada com sucesso!'})

@app.route('/adicionar_segredo', methods=['POST'])
def adicionar_segredo():
    dados = request.json
    aplicacao_id = dados['aplicacao_id']
    novo_segredo = Segredo(chave=dados['chave'], valor=dados['valor'], aplicacao_id=aplicacao_id)
    db.session.add(novo_segredo)
    db.session.commit()
    return jsonify({'mensagem': 'Segredo adicionado com sucesso!'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

