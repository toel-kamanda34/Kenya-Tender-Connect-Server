#!/usr/bin/env python3
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.extensions import db

def setup_database():
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✅ Database tables created successfully!")
        
        # Create a default admin user
        from app.models import User
        
        admin = User.query.filter_by(email='admin@tenderconnect.com').first()
        if not admin:
            admin = User(
                email='admin@tenderconnect.com',
                full_name='System Administrator',
                phone='+254700000000',
                role='admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("✅ Default admin user created!")
            print("   Email: admin@tenderconnect.com")
            print("   Password: admin123")
        else:
            print("ℹ️  Admin user already exists")

if __name__ == '__main__':
    setup_database()
