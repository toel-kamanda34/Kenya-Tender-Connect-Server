# Kenya Tender Connect - Backend Server

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green?logo=flask)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-5.7+-blue?logo=mysql)](https://www.mysql.com/)

Backend API for the **Kenya Tender Connect** platform built with **Flask, MySQL, and JWT authentication**.

---

## Features

* 🔐 JWT Authentication & Authorization
* 📋 Tender Management (CRUD operations)
* 📄 Application Management
* 👥 User Management
* 📁 Document Upload Support
* 🌐 RESTful API

---

## Tech Stack

* **Backend:** Flask, Python
* **Database:** MySQL with SQLAlchemy ORM
* **Authentication:** JWT with Flask-JWT-Extended
* **File Upload:** Secure document handling
* **CORS:** Cross-Origin Resource Sharing enabled

---

## Quick Start

### Prerequisites

* Python 3.8+
* MySQL 5.7+
* `pip` (Python package manager)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/toel-kamanda34/kenya-tender-connect-server.git
cd kenya-tender-connect-server
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

```bash
cp .env.example .env
# Edit .env with your database credentials and secret keys
```

5. **Set up database**

```bash
python scripts/setup_db.py
```

6. **Seed sample data (optional)**

```bash
python scripts/seed_data.py
```

7. **Run the application**

```bash
python run.py
```

The API will be available at: `http://localhost:5000`

---

## API Endpoints

### Authentication

| Method | Endpoint             | Description       |
| ------ | -------------------- | ----------------- |
| POST   | `/api/auth/register` | User registration |
| POST   | `/api/auth/login`    | User login        |
| GET    | `/api/auth/me`       | Get current user  |

### Tenders

| Method | Endpoint            | Description                     |
| ------ | ------------------- | ------------------------------- |
| GET    | `/api/tenders`      | List all tenders (with filters) |
| GET    | `/api/tenders/<id>` | Get tender details              |
| POST   | `/api/tenders`      | Create new tender (admin)       |
| PUT    | `/api/tenders/<id>` | Update tender (admin)           |
| DELETE | `/api/tenders/<id>` | Delete tender (admin)           |

### Applications

| Method | Endpoint                        | Description             |
| ------ | ------------------------------- | ----------------------- |
| GET    | `/api/applications`             | Get user's applications |
| POST   | `/api/applications`             | Create new application  |
| PUT    | `/api/applications/<id>`        | Update application      |
| POST   | `/api/applications/<id>/submit` | Submit application      |

---

## Environment Variables

Create a `.env` file with the following:

```env
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
DATABASE_URL=mysql+pymysql://username:password@localhost/kenya_tender_db
FLASK_CONFIG=development
```

---

## Database Schema

The application uses the following main tables:

* `users` - User accounts and profiles
* `tenders` - Tender listings and details
* `applications` - User applications for tenders

---

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Database Migrations

```bash
flask db init
flask db migrate -m "Migration message"
flask db upgrade
```

---

## Deployment

The application can be deployed to various platforms:

* **Railway:** Easy Flask deployment
* **Heroku:** Traditional PaaS
* **AWS Elastic Beanstalk:** AWS deployment
* **DigitalOcean App Platform:** Simple app deployment

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---

## Support

For support:

* Email: [toelokemwa@gmail.com](mailto:toelokemwa@gmail.com)
* Or create an issue in the repository





