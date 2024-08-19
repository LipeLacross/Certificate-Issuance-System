from flask import Blueprint, jsonify, request
from app.models import Certificado
from app.database import db

bp = Blueprint('certificados', __name__, url_prefix='/api/certificados')

# Rota para listar todos os certificados (GET)
@bp.route('', methods=['GET'])
def get_certificados():
    certificados = Certificado.query.all()
    result = [
        {
            'id': c.id,
            'nome': c.nome,
            'curso': c.curso,
            'data_emissao': c.data_emissao.strftime('%Y-%m-%d')
        } for c in certificados
    ]
    return jsonify(result)

# Rota para adicionar um novo certificado (POST)
@bp.route('', methods=['POST'])
def add_certificado():
    data = request.get_json()
    novo_certificado = Certificado(
        nome=data['nome'],
        curso=data['curso'],
        data_emissao=data['data_emissao']
    )
    db.session.add(novo_certificado)
    db.session.commit()
    return jsonify({'message': 'Certificado adicionado com sucesso!'}), 201

# Rota para obter detalhes de um certificado específico (GET)
@bp.route('/<int:id>', methods=['GET'])
def get_certificado(id):
    certificado = Certificado.query.get_or_404(id)
    result = {
        'id': certificado.id,
        'nome': certificado.nome,
        'curso': certificado.curso,
        'data_emissao': certificado.data_emissao.strftime('%Y-%m-%d')
    }
    return jsonify(result)

# Rota para atualizar um certificado específico (PUT)
@bp.route('/<int:id>', methods=['PUT'])
def update_certificado(id):
    certificado = Certificado.query.get_or_404(id)
    data = request.get_json()
    certificado.nome = data.get('nome', certificado.nome)
    certificado.curso = data.get('curso', certificado.curso)
    certificado.data_emissao = data.get('data_emissao', certificado.data_emissao)

    db.session.commit()
    return jsonify({'message': 'Certificado atualizado com sucesso!'})

# Rota para deletar um certificado específico (DELETE)
@bp.route('/<int:id>', methods=['DELETE'])
def delete_certificado(id):
    certificado = Certificado.query.get_or_404(id)
    db.session.delete(certificado)
    db.session.commit()
    return jsonify({'message': 'Certificado deletado com sucesso!'})
