# Feedback System
A clean and user-friendly web application built using Django + Bootstrap to enable structured internal feedback between managers and employees.

## Key Features

- Role-based login (Employee & Manager)
- Employees can:
     View feedback given by managers
     Acknowledge and comment on feedback
- Managers can:
     Assign feedback to employees
     View acknowledgment and comments
     Manager dashboard for team overview
     Employee signup with restricted manager access
     Dockerized backend

## Technologies Used

    LAYER      |    STACK                                    

    Backend    |    Python, Django                           
    Frontend   |    Django Templates + Bootstrap 5           
    Database   |    SQLite                                   
    Deployment |    Docker (backend only)                    
    Auth       |    Django built-in auth (Custom user model) 

## Project Structure
feedbacksystem_project/
│
├── feedbacksystem/ # Django project settings
├── feedback/ # Core app (models, views, urls)
├── templates/ # Bootstrap-powered UI
├── Dockerfile # Docker config for backend
├── requirements.txt
└── README.md

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/your-username/feedbacksystem_project.git
cd feedbacksystem_project
### 2. Create a Virtual Environment
python -m venv venv
For Windows: venv\Scripts\activate
### 3. Install Required Packages
pip install -r requirements.txt
### 4. Apply Migrations
python manage.py makemigrations
python manage.py migrate
### 5. Create a Superuser
python manage.py createsuperuser
### 6. Run the Project
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to use the system.


## Docker Backend Setup
# Step 1: Build Docker Image
docker build -t feedback-backend .
# Step 2: 
Option A: Run on Default Port (if 8000 is free)
docker run -d -p 8000:8000 feedback-backend
Then access your app at: http://localhost:8000
Option B: If Port 8000 is in use (use another port like 8080)
docker run -d -p 8080:8000 feedback-backend
Then access your app at:http://localhost:8080


## Design Decisions
Used Django’s custom user model for separating employee/manager access
Manager cannot sign up through UI (admin created only)
Simple SQLite DB chosen for lightweight and quick development
Dockerized only the backend (as per assignment requirement)
Kept UI minimal, clean, and mobile-friendly with Bootstrap
Added acknowledgment tracking for manager clarity

## Notes
AI tools were used for some design suggestions and UI alignment.
All core logic and integration were developed and tested manually.
Backend is Dockerized as required. Frontend uses Django templates.

## Author
Syeda Arfain Fathima
[arfainsyed09@gmail.com]
[http://linkedin.com/in/arfainsyed]

## License
This project is licensed under the MIT License.


