# Project Management Dashboard

A web-based project management application built with Flask and Python that allows users to create projects, manage tasks, and track project progress through a simple dashboard interface.

## Features

### Project Management
- Create new projects
- Edit existing projects
- Delete projects
- View project details
- Track project status

### Task Management
- Create tasks within projects
- Assign task priorities
- Set task due dates
- Update task status
- Delete tasks

### Progress Tracking
- Automatic project completion percentage
- Dashboard progress indicators
- Real-time progress calculations based on completed tasks

### Dashboard
- Total project count
- Active project count
- Completed project count
- Project progress overview
- Responsive Bootstrap interface

---

## Technology Stack

### Backend
- Python
- Flask
- SQLAlchemy
- Flask-WTF

### Frontend
- HTML
- Jinja2 Templates
- Bootstrap 5

### Database
- SQLite

### Development Tools
- Git
- GitHub

---

## Project Structure

```text
project-management-dashboard/
│
├── app/
│   ├── forms/
│   │   ├── project_form.py
│   │   └── task_form.py
│   │
│   ├── models/
│   │   ├── project.py
│   │   └── task.py
│   │
│   ├── routes/
│   │   ├── dashboard.py
│   │   └── projects.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── projects.html
│   │   ├── project_detail.html
│   │   ├── create_project.html
│   │   └── edit_project.html
│   │
│   ├── extensions.py
│   └── __init__.py
│
├── run.py
├── create_db.py
├── requirements.txt
└── README.md
```

---

## Installation

1. Clone the Repository

```bash
git clone https://github.com/James2c/project-management-dashboard.git
cd project-management-dashboard
```

2. Create a Virtual Environment

```bash
python -m venv .venv
```

3. Activate the environment:

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

4. Install Dependencies

```bash
pip install -r requirements.txt
```

5. Create the Database

```bash
python create_db.py
```

6. Run the Application

```bash
python run.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

## Current Features

- [x] Project CRUD Operations
- [x] Task CRUD Operations
- [x] Project-to-Task Relationships
- [x] Dashboard Metrics
- [x] Progress Tracking
- [x] Bootstrap UI

---


### Future Improvements
- Overdue task detection
- Dashboard alerts
- Task filtering
- Kanban board view
- Search functionality
- REST API
- Email notifications
- Project reporting

---

## Learning Objectives

This project was created to strengthen practical experience with:

- Flask
- Databases
- Routes
- Templates
- SQLAlchemy ORM
- Bootstrap UI development
- CRUD application design
- Git and GitHub workflows

---

## License

This project is available for educational and portfolio purposes.