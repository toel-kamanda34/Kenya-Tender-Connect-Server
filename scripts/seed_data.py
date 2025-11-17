#!/usr/bin/env python3
import sys
import os
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.extensions import db
from app.models import Tender

def seed_sample_tenders():
    app = create_app()
    
    with app.app_context():
        # Sample tenders data
        sample_tenders = [
            {
                'title': 'Supply of Office Furniture to Nairobi County',
                'description': 'Supply and delivery of modern office furniture including desks, chairs, and cabinets for Nairobi County offices.',
                'category': 'Supplies',
                'county': 'Nairobi',
                'tender_number': 'NBI/OF/2024/001',
                'procurement_entity': 'Nairobi County Government',
                'value': 2500000.00,
                'closing_date': datetime.utcnow() + timedelta(days=30),
                'status': 'active',
                'requirements': 'Valid business registration, Tax compliance certificate, AGPO certificate for youth/women/PWDs'
            },
            {
                'title': 'Construction of Community Water Project in Kisumu',
                'description': 'Construction of a community water project including borehole drilling, water tank installation, and distribution system.',
                'category': 'Construction',
                'county': 'Kisumu',
                'tender_number': 'KSM/WATER/2024/002',
                'procurement_entity': 'Kisumu County Government',
                'value': 5000000.00,
                'closing_date': datetime.utcnow() + timedelta(days=45),
                'status': 'active',
                'requirements': 'NCA registration, Valid business registration, Tax compliance certificate, AGPO certificate'
            },
            {
                'title': 'Provision of IT Equipment to Mombasa County',
                'description': 'Supply and installation of computer systems, printers, and networking equipment for county offices.',
                'category': 'ICT',
                'county': 'Mombasa',
                'tender_number': 'MBA/IT/2024/003',
                'procurement_entity': 'Mombasa County Government',
                'value': 3500000.00,
                'closing_date': datetime.utcnow() + timedelta(days=20),
                'status': 'active',
                'requirements': 'Valid business registration, Tax compliance certificate, AGPO certificate, Proof of similar previous work'
            }
        ]
        
        for tender_data in sample_tenders:
            # Check if tender already exists
            existing = Tender.query.filter_by(tender_number=tender_data['tender_number']).first()
            if not existing:
                tender = Tender(**tender_data)
                db.session.add(tender)
        
        db.session.commit()
        print(f"✅ {len(sample_tenders)} sample tenders added to database!")

if __name__ == '__main__':
    seed_sample_tenders()
