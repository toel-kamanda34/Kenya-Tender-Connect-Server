from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return jsonify({
        'message': 'Kenya Tender Connect API is running! 🚀',
        'version': '1.0.0',
        'status': 'active',
        'endpoints': {
            'auth': '/api/auth',
            'tenders': '/api/tenders',
            'applications': '/api/applications'
        }
    })

@main_bp.route('/api')
def api_info():
    return jsonify({
        'name': 'Kenya Tender Connect API',
        'description': 'Backend for Kenya Tender Connect Platform',
        'endpoints': {
            'register': 'POST /api/auth/register',
            'login': 'POST /api/auth/login',
            'get_profile': 'GET /api/auth/me',
            'list_tenders': 'GET /api/tenders',
            'get_tender': 'GET /api/tenders/<id>',
            'create_application': 'POST /api/applications',
            'get_applications': 'GET /api/applications'
        }
    })

