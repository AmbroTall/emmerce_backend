# CRM Application

## Overview
This is a mini CRM application built with **Django** (backend) for managing leads, contacts, notes, and reminders. The application also includes a statistics dashboard to provide insights.

## Features

### Backend
- **Leads**: Create, read, update, delete (CRUD) operations.
- **Contacts**: CRUD operations with linkage to leads.
- **Notes**: Add notes for specific leads.
- **Reminders**: Schedule and manage reminders with asynchronous task handling using **Celery** and **Redis**.
- **Statistics API**: Endpoints to retrieve aggregated data for leads, contacts, notes, and reminders.

## Installation

### Prerequisites
- Python 3.8+
- Redis server
- Git

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crm-backend.git
   cd crm-backend

2. Create a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Configure environment variables:
   ```bash
   Create a .env file in the root directory and add the following:

   DJANGO_SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=*
   DATABASE_URL=sqlite:///db.sqlite3
   REDIS_URL=redis://localhost:6379/0

5. Apply migrations:
   ```bash
   python manage.py migrate

6. Run the development server:
   ```bash
   python manage.py runserver

7. Start Redis and Celery

- Start the Redis server:
   ```bash
   redis-server

8. Start the Celery worker:
   ```bash
   celery -A core worker --loglevel=info

9. Start the Celery beat scheduler:
   ```bash
   celery -A core beat --loglevel=info

10. Access the Application

- Backend: http://127.0.0.1:8000

# API Endpoints

### CRUD Endpoints
```
   Leads: /leads/
   
   Contacts: /contacts/
   
   Notes: /notes/
   
   Reminders: /reminders/
```

## Statistics Endpoints
```
Lead Statistics: /stats/leads/

Contact Statistics: /stats/contacts/

Note Statistics: /stats/notes/

Reminder Statistics: /stats/reminders/
```

# Running Tests

## Backend Tests

- Activate the virtual environment:
   ```bash
   source .venv/bin/activate

- Run the test suite using pytest:
   ```bash
   pytest



