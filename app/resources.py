from flask_restful import Resource, reqparse
from app.models import Certificate
from app.database import db  # Importa db diretamente do novo módulo

class CertificateResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True, help='Name of the certificate')
        self.parser.add_argument('issued_date', type=str, required=True, help='Issued date of the certificate')
        self.parser.add_argument('valid_until', type=str, required=True, help='Validity date of the certificate')

    def post(self):
        args = self.parser.parse_args()
        certificate = Certificate(
            name=args['name'],
            issued_date=args['issued_date'],
            valid_until=args['valid_until']
        )
        db.session.add(certificate)
        db.session.commit()
        return {'message': 'Certificate created'}, 201

    def get(self, cert_id):
        certificate = Certificate.query.get(cert_id)
        if not certificate:
            return {'message': 'Certificate not found'}, 404
        return {
            'id': certificate.id,
            'name': certificate.name,
            'issued_date': str(certificate.issued_date),
            'valid_until': str(certificate.valid_until)
        }
