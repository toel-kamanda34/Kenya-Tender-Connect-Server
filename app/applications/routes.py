from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models import Application, Tender, User

applications_bp = Blueprint('applications', __name__)

@applications_bp.route('', methods=['GET'])
@jwt_required()
def get_user_applications():
    try:
        user_id = get_jwt_identity()
        applications = Application.query.filter_by(user_id=user_id).all()
        
        return jsonify({
            'applications': [app.to_dict() for app in applications]
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@applications_bp.route('', methods=['POST'])
@jwt_required()
def create_application():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        if not data.get('tender_id'):
            return jsonify({'error': 'tender_id is required'}), 400
        
        # Check if tender exists
        tender = Tender.query.get(data['tender_id'])
        if not tender:
            return jsonify({'error': 'Tender not found'}), 404
        
        # Check if user already applied
        existing_application = Application.query.filter_by(
            user_id=user_id, tender_id=data['tender_id']
        ).first()
        
        if existing_application:
            return jsonify({'error': 'You have already applied for this tender'}), 400
        
        # Create application
        application = Application(
            user_id=user_id,
            tender_id=data['tender_id'],
            status='draft',
            documents=data.get('documents', '[]')
        )
        
        db.session.add(application)
        db.session.commit()
        
        return jsonify({
            'message': 'Application created successfully',
            'application': application.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@applications_bp.route('/<int:application_id>', methods=['PUT'])
@jwt_required()
def update_application(application_id):
    try:
        user_id = get_jwt_identity()
        application = Application.query.get_or_404(application_id)
        
        # Check if user owns this application
        if application.user_id != user_id:
            return jsonify({'error': 'Access denied'}), 403
        
        data = request.get_json()
        
        # Update fields
        if 'documents' in data:
            application.documents = data['documents']
        if 'status' in data:
            application.status = data['status']
            if data['status'] == 'submitted':
                application.submission_date = db.func.now()
        
        db.session.commit()
        
        return jsonify({
            'message': 'Application updated successfully',
            'application': application.to_dict()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@applications_bp.route('/<int:application_id>/submit', methods=['POST'])
@jwt_required()
def submit_application(application_id):
    try:
        user_id = get_jwt_identity()
        application = Application.query.get_or_404(application_id)
        
        # Check if user owns this application
        if application.user_id != user_id:
            return jsonify({'error': 'Access denied'}), 403
        
        # Update application status
        application.status = 'submitted'
        application.submission_date = db.func.now()
        
        db.session.commit()
        
        return jsonify({
            'message': 'Application submitted successfully',
            'application': application.to_dict()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
