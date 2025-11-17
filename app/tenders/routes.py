from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models import Tender

tenders_bp = Blueprint('tenders', __name__)

@tenders_bp.route('', methods=['GET'])
def get_tenders():
    try:
        # Get query parameters
        category = request.args.get('category')
        county = request.args.get('county')
        status = request.args.get('status', 'active')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        
        # Build query
        query = Tender.query
        
        if category:
            query = query.filter(Tender.category == category)
        if county:
            query = query.filter(Tender.county == county)
        if status:
            query = query.filter(Tender.status == status)
        
        # Paginate results
        tenders = query.order_by(Tender.closing_date.asc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'tenders': [tender.to_dict() for tender in tenders.items],
            'total': tenders.total,
            'pages': tenders.pages,
            'current_page': page
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@tenders_bp.route('/<int:tender_id>', methods=['GET'])
def get_tender(tender_id):
    try:
        tender = Tender.query.get_or_404(tender_id)
        return jsonify({'tender': tender.to_dict()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@tenders_bp.route('', methods=['POST'])
@jwt_required()
def create_tender():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['title', 'description', 'closing_date', 'category', 'county']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} is required'}), 400
        
        # Create new tender
        tender = Tender(
            title=data['title'],
            description=data['description'],
            category=data['category'],
            county=data['county'],
            tender_number=data.get('tender_number'),
            procurement_entity=data.get('procurement_entity'),
            value=data.get('value'),
            closing_date=data['closing_date'],
            status=data.get('status', 'active'),
            requirements=data.get('requirements')
        )
        
        db.session.add(tender)
        db.session.commit()
        
        return jsonify({
            'message': 'Tender created successfully',
            'tender': tender.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@tenders_bp.route('/<int:tender_id>', methods=['PUT'])
@jwt_required()
def update_tender(tender_id):
    try:
        tender = Tender.query.get_or_404(tender_id)
        data = request.get_json()
        
        # Update fields
        updatable_fields = ['title', 'description', 'category', 'county', 'tender_number',
                          'procurement_entity', 'value', 'closing_date', 'status', 'requirements']
        
        for field in updatable_fields:
            if field in data:
                setattr(tender, field, data[field])
        
        db.session.commit()
        
        return jsonify({
            'message': 'Tender updated successfully',
            'tender': tender.to_dict()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@tenders_bp.route('/<int:tender_id>', methods=['DELETE'])
@jwt_required()
def delete_tender(tender_id):
    try:
        tender = Tender.query.get_or_404(tender_id)
        
        db.session.delete(tender)
        db.session.commit()
        
        return jsonify({'message': 'Tender deleted successfully'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
