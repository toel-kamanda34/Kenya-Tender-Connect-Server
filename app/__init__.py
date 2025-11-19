from flask import Flask
from flask_cors import CORS
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Enable CORS with specific origins
    CORS(app, 
         origins=["http://127.0.0.1:5500", "http://localhost:5500", "http://localhost:3000", "http://127.0.0.1:3000"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Origin"],
         supports_credentials=True)
    
    # Initialize extensions
    from .extensions import db, migrate, jwt
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Register blueprints
    from .auth.routes import auth_bp
    from .tenders.routes import tenders_bp
    from .applications.routes import applications_bp
    
    # Try to import main routes if they exist
    try:
        from .routes import main_bp
        app.register_blueprint(main_bp)
    except ImportError:
        print("Main routes not found - creating basic route")
        @app.route('/')
        def index():
            return {"message": "Kenya Tender Connect API is running!"}
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(tenders_bp, url_prefix='/api/tenders')
    app.register_blueprint(applications_bp, url_prefix='/api/applications')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app
