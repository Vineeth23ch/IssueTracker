# Issue & Vulnerability Tracking System

## Overview

This project is a RESTful API built using **Python Flask** and **SQLite** to manage software issues and security vulnerabilities. It supports CRUD operations, validation, filtering, sorting, and reporting.

## Technologies

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Flask-CORS
* Git & GitHub
* Postman

## Features

* Create, Read, Update, Delete vulnerabilities
* Input validation
* Filter by severity and status
* Sort records
* Summary report API
* SQLite database

## Project Structure

```text
IssueTracker/
│
├── app.py
├── config.py
├── database.py
├── models/
├── routes/
├── services/
├── utils/
├── instance/
└── README.md
```

## API Endpoints

| Method | Endpoint                | Description             |
| ------ | ----------------------- | ----------------------- |
| GET    | `/`                     | Health check            |
| GET    | `/vulnerabilities`      | Get all vulnerabilities |
| GET    | `/vulnerabilities/<id>` | Get vulnerability by ID |
| POST   | `/vulnerabilities`      | Create vulnerability    |
| PUT    | `/vulnerabilities/<id>` | Update vulnerability    |
| DELETE | `/vulnerabilities/<id>` | Delete vulnerability    |
| GET    | `/report`               | Summary report          |

## Setup

```bash
git clone <repository-url>
cd IssueTracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

API runs at:

```text
http://127.0.0.1:5000
```

## Testing

The APIs were tested using **Postman**.

## Future Improvements

* User authentication
* Dashboard UI
* File attachments
* Export to CSV/PDF
