from flask import Blueprint, jsonify, request
from app.models import Certificado
from app.database import db

bp = Blueprint('certificados', __name__, url_prefix='/api/certificados')

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
