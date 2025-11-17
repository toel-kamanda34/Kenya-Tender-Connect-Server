from .extensions import db
from datetime import datetime
import bcrypt

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    role = db.Column(db.String(20), default='youth')  # youth, admin, mentor, sacco
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    applications = db.relationship('Application', backref='applicant', lazy=True)
    
    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'full_name': self.full_name,
            'phone': self.phone,
            'role': self.role,
            'created_at': self.created_at.isoformat()
        }

class Tender(db.Model):
    __tablename__ = 'tenders'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    county = db.Column(db.String(100))
    tender_number = db.Column(db.String(100), unique=True)
    procurement_entity = db.Column(db.String(255))
    value = db.Column(db.Numeric(15, 2))
    published_date = db.Column(db.DateTime)
    closing_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default='active')  # active, closed, cancelled
    requirements = db.Column(db.Text)  # JSON string of requirements
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    applications = db.relationship('Application', backref='tender', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'county': self.county,
            'tender_number': self.tender_number,
            'procurement_entity': self.procurement_entity,
            'value': float(self.value) if self.value else None,
            'published_date': self.published_date.isoformat() if self.published_date else None,
            'closing_date': self.closing_date.isoformat(),
            'status': self.status,
            'requirements': self.requirements,
            'created_at': self.created_at.isoformat()
        }

class Application(db.Model):
    __tablename__ = 'applications'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tender_id = db.Column(db.Integer, db.ForeignKey('tenders.id'), nullable=False)
    status = db.Column(db.String(50), default='draft')  # draft, submitted, under_review, awarded, rejected
    submission_date = db.Column(db.DateTime)
    documents = db.Column(db.Text)  # JSON string of document paths
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'tender_id': self.tender_id,
            'status': self.status,
            'submission_date': self.submission_date.isoformat() if self.submission_date else None,
            'documents': self.documents,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
