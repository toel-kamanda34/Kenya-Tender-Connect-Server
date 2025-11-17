from flask import Flask
from flask_cors import CORS
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    from .extensions import db, migrate, jwt
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    
    # Register blueprints
    from .auth.routes import auth_bp
    from .tenders.routes import tenders_bp
    from .applications.routes import applications_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(tenders_bp, url_prefix='/api/tenders')
    app.register_blueprint(applications_bp, url_prefix='/api/applications')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app
