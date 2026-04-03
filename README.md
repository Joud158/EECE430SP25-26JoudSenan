# Voley Player List - Assignment 4

## Description
A simple Django CRUD web application to manage volleyball players.  
The project supports creating, viewing, updating, and deleting player records through a basic styled interface.

## Requirements
- Python
- Django

## How to run
1. Open terminal in this project folder.
2. Create and activate a virtual environment.
3. Install Django:

```bash
pip install django
```

4. Run:

```bash
python manage.py migrate
python manage.py runserver
```

5. Open:

```text
http://127.0.0.1:8000/
```

## Features
- Add player
- View players
- Update player
- Delete player
- Basic input validation
- Error messages using Django messages
- Simple pink modern UI

## Player Fields
- ID
- Name
- Date Joined
- Position
- Salary/Payment
- Contact Person
