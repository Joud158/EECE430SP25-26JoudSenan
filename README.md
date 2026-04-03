# Volley Player List - Dockerized Django CRUD Application

## Description
A simple Django CRUD web application to manage volleyball players.

The system allows the user to create, view, update, and delete player records through a styled web interface.  
This project was dockerized so it can run consistently without requiring manual local dependency setup.

## Features
- Add player
- View players
- Update player
- Delete player
- Basic input validation
- Error messages using Django messages
- Simple modern UI

## Player Fields
- ID
- Name
- Date Joined
- Position
- Salary / Payment
- Contact Person

## Requirements
To run this project using Docker, make sure the following is installed:

- Docker Desktop

## How to Run Using Docker

### 1. Open Docker Desktop
Make sure Docker Desktop is installed and running before executing any Docker commands.

### 2. Open terminal in the project folder
Navigate to the folder that contains:
- `manage.py`
- `Dockerfile`
- `requirements.txt`

### 3. Build the Docker image
Run the following command:

```bash
docker build -t volley-player-app .
```

### 4. Run the Docker container
Run the following command:

```bash
docker run -d -p 8000:8000 --name volley-player-container volley-player-app
```

### 5. Open the application
Open your browser and go to:

```text
http://localhost:8000/
```
