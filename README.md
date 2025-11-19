# Kenya Tender Connect - Backend Server

Backend API for Kenya Tender Connect platform built with Flask, MySQL, and JWT authentication.

## Features

- 🔐 JWT Authentication & Authorization
- 📋 Tender Management (CRUD operations)
- 📄 Application Management
- 👥 User Management
- 📁 Document Upload Support
- 🌐 RESTful API

## Tech Stack

- **Backend**: Flask, Python
- **Database**: MySQL with SQLAlchemy ORM
- **Authentication**: JWT with Flask-JWT-Extended
- **File Upload**: Secure document handling
- **CORS**: Cross-Origin Resource Sharing enabled

## Quick Start

### Prerequisites

- Python 3.8+
- MySQL 5.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/toel-kamanda34/kenya-tender-connect-server.git
   cd kenya-tender-connect-server
2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies**

```bash
pip install -r requirements.txt
4. **Set up environment variables**

```bash
cp .env.example .env
# Edit .env with your database credentials and secret keys
Set up database

bash
python scripts/setup_db.py
Seed sample data (optional)

bash
python scripts/seed_data.py
Run the application

bash
python run.py
The API will be available at http://localhost:5000

API Endpoints
Authentication
POST /api/auth/register - User registration

POST /api/auth/login - User login

GET /api/auth/me - Get current user

Tenders
GET /api/tenders - List all tenders (with filters)

GET /api/tenders/<id> - Get tender details

POST /api/tenders - Create new tender (admin)

PUT /api/tenders/<id> - Update tender (admin)

DELETE /api/tenders/<id> - Delete tender (admin)

Applications
GET /api/applications - Get user's applications

POST /api/applications - Create new application

PUT /api/applications/<id> - Update application

POST /api/applications/<id>/submit - Submit application

Environment Variables
Create a .env file with the following variables:

env
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
DATABASE_URL=mysql+pymysql://username:password@localhost/kenya_tender_db
FLASK_CONFIG=development
Database Schema
The application uses the following main tables:

users - User accounts and profiles

tenders - Tender listings and details

applications - User applications for tenders

Development
Running Tests
bash
python -m pytest tests/
Database Migrations
bash
flask db init
flask db migrate -m "Migration message"
flask db upgrade
Deployment
The application can be deployed to various platforms:

Railway: Easy Flask deployment

Heroku: Traditional PaaS

AWS Elastic Beanstalk: AWS deployment

DigitalOcean App Platform: Simple app deployment

Contributing
Fork the repository

Create a feature branch

Commit your changes

Push to the branch

Create a Pull Request

License
This project is licensed under the MIT License.

Support
For support, email toelokemwa@gmail.com or create an issue in the repository.



