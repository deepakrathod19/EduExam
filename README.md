# 📝 Exam System (Django)

A web-based examination management system built with **Django** backend, **HTML/CSS** frontend, and **MySQL** database. This application streamlines exam creation, management, and student examination with an intuitive interface for educators and students.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Project Structure](#project-structure)
- [Database Configuration](#database-configuration)
- [Running the Application](#running-the-application)
- [Usage Guide](#usage-guide)
- [Project URLs](#project-urls)
- [Django Models & Database](#django-models--database)
- [Static Files & CSS](#static-files--css)
- [Common Issues & Troubleshooting](#common-issues--troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact & Support](#contact--support)

---

## Overview

The **Exam System** is a Django-based web application designed for educational institutions and testing centers. It provides:

- **For Educators**: Create exams, manage questions, configure exam settings, and view student results
- **For Students**: Take exams with timed sessions, review answers, and access results
- **For Administrators**: Manage users, monitor system performance, and generate reports

Built with Django's robust framework, HTML/CSS for responsive frontend, and MySQL for reliable data storage.

---

## Features

### ✨ Core Features

- **Exam Management**
  - Create, edit, and delete exams
  - Set exam duration, passing scores, and attempt limits
  - Schedule exams with specific date/time constraints
  - Support for multiple question types (MCQ, True/False, Short Answer)

- **Question Bank Management**
  - Organize questions by categories and difficulty levels
  - Add explanations and references for each question
  - Easy question addition and editing interface
  - Search and filter questions functionality

- **Student Examination**
  - Secure, timed exam interface
  - Auto-save functionality to prevent data loss
  - Real-time timer display
  - Question navigation with progress tracking
  - Bookmark important questions for review

- **Result & Analytics**
  - Instant result display with detailed breakdowns
  - Question-wise performance analysis
  - Score reports for educators
  - Student performance history

- **User Management**
  - Role-based access control (Admin, Educator, Student)
  - User authentication with Django's built-in system
  - Profile management and password reset
  - User registration and enrollment

- **Security Features**
  - CSRF protection (Django middleware)
  - Secure password hashing
  - Session-based authentication
  - Permission-based access control

---

## Tech Stack

### Backend
- **Django** (v5.2.3) - Web framework for Python
- **Django REST Framework** (Optional API support)
- **PyMySQL** - MySQL database adapter for Python

### Frontend
- **HTML5** - Markup language
- **CSS3** - Styling and layout
- **JavaScript** (Vanilla/Optional) - Interactive features
- **Bootstrap** (Optional CSS framework)

### Database
- **MySQL** (v5.7+) - Relational database management system
- **Django ORM** - Object-Relational Mapping

### Additional Tools
- **Git & GitHub** - Version control
- **Django Admin** - Built-in admin interface
- **Django Templates** - Server-side rendering

---

## Prerequisites

Before you begin, ensure you have the following installed:

### Required Software
- **Python** (v3.10 or higher) - [Download](https://www.python.org/downloads/)
- **MySQL** (v5.7 or higher) - [Download](https://dev.mysql.com/downloads/mysql/)
- **Git** - [Download](https://git-scm.com/)
- **pip** (Python package manager) - Comes with Python

### System Requirements
- **OS**: Windows, macOS, or Linux
- **RAM**: Minimum 2GB (4GB recommended)
- **Storage**: 500MB free disk space
- **Code Editor**: VS Code recommended

### Verify Installations
```bash
# Check Python
python --version
# Expected: Python 3.10.0 or higher

# Check pip
pip --version
# Expected: pip 21.0 or higher

# Check MySQL
mysql --version
# Expected: MySQL 5.7.0 or higher
```

---

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/deepakrathod19/project2.git
cd project2
```

### Step 2: Create Python Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Required Python Packages

```bash
# Upgrade pip first
pip install --upgrade pip

# Install dependencies
pip install Django==5.2.3
pip install djangorestframework
pip install PyMySQL
```

Or use requirements.txt if available:
```bash
pip install -r requirements.txt
```

### Step 4: Create MySQL Database

```bash
# Login to MySQL
mysql -u root -p

# Inside MySQL prompt:
CREATE DATABASE 1276db;
CREATE USER 'root'@'localhost' IDENTIFIED BY 'root123';
GRANT ALL PRIVILEGES ON 1276db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

Or using MySQL Workbench:
1. Open MySQL Workbench
2. Create new schema: `1276db`
3. Create user with username `root` and password `root123`
4. Grant all privileges on `1276db` to this user

### Step 5: Configure Django Settings

The project is already configured in `project2/settings.py`:

```python
# Database configuration (already set in settings.py)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '1276db',
        'USER': 'root',
        'PASSWORD': 'root123',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'examapp',
    'rest_framework'
]
```

### Step 6: Apply Database Migrations

```bash
# Create migrations for apps
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
# Follow prompts to create admin user
```

### Step 7: Collect Static Files

```bash
# Collect static files (CSS, JS, images)
python manage.py collectstatic --noinput
```

---

## Project Structure

```
project2/
│
├── manage.py                    # Django command-line tool
│
├── project2/                    # Project configuration folder
│   ├── __init__.py
│   ├── settings.py              # Project settings
│   ├── urls.py                  # URL routing configuration
│   ├── asgi.py                  # ASGI configuration
│   └── wsgi.py                  # WSGI configuration
│
├── examapp/                     # Main Django app
│   ├── migrations/              # Database migrations
│   │   └── __init__.py
│   │
│   ├── static/                  # Static files (CSS, JS, images)
│   │   ├── css/
│   │   │   └── style.css        # Custom styles
│   │   ├── js/
│   │   │   └── script.js        # JavaScript files
│   │   └── images/              # Image files
│   │
│   ├── templates/               # HTML templates
│   │   ├── base.html            # Base template
│   │   ├── home.html            # Home page
│   │   ├── exam_list.html       # Exam listing
│   │   ├── exam_detail.html     # Exam details
│   │   ├── exam_taker.html      # Exam taking interface
│   │   ├── results.html         # Results display
│   │   └── login.html           # Login page
│   │
│   ├── models.py                # Database models
│   ├── views.py                 # View functions
│   ├── urls.py                  # App URL configuration
│   ├── admin.py                 # Django admin configuration
│   └── forms.py                 # Django forms (if any)
│
├── db.sqlite3                   # SQLite DB (not used, MySQL instead)
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## Database Configuration

### MySQL Connection Details

Current database configuration in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '1276db',           # Database name
        'USER': 'root',             # MySQL username
        'PASSWORD': 'root123',      # MySQL password
        'HOST': 'localhost',        # Database host
        'PORT': '3306'              # MySQL port
    }
}
```

### Database Models (examapp/models.py)

Expected models for exam system:

```python
from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes
    passing_score = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.TextField()
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=1)
    explanation = models.TextField(blank=True)

class StudentExam(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    submitted_at = models.DateTimeField(null=True)
    score = models.IntegerField(null=True)
    status = models.CharField(max_length=20)  # 'ongoing', 'submitted', etc.
```

---

## Running the Application

### Development Server

```bash
# Start Django development server
python manage.py runserver

# Server will run at: http://127.0.0.1:8000/
```

### Access the Application

- **Home Page**: `http://localhost:8000/examapp/`
- **Admin Panel**: `http://localhost:8000/admin/`
- **Exam Portal**: `http://localhost:8000/examapp/exams/`

### Create Superuser for Admin Access

```bash
python manage.py createsuperuser
# Enter username, email, password when prompted
```

---

## Usage Guide

### For Educators

1. **Login to Admin Panel** (`/admin/`)
   - Create exam using Django admin
   - Add questions to exam
   - Set exam duration and passing score

2. **Create New Exam**
   - Go to Exam list
   - Click "Create New Exam"
   - Fill in exam details (title, description, duration)
   - Add questions with options and correct answers

3. **Manage Questions**
   - Add individual questions
   - Edit existing questions
   - Delete unwanted questions
   - View question explanations

4. **View Results**
   - Check student responses
   - View score breakdowns
   - Access result statistics

### For Students

1. **Register/Login**
   - Create student account
   - Login with credentials

2. **Browse Exams**
   - View available exams
   - Check exam duration and details

3. **Take Exam**
   - Click "Start Exam"
   - Answer all questions
   - Review answers before submission
   - Submit exam

4. **View Results**
   - Check score immediately after submission
   - Review correct answers and explanations
   - View performance summary

### For Administrators

1. **User Management**
   - Create/manage educator accounts
   - Create/manage student accounts
   - Assign user roles

2. **System Configuration**
   - Configure exam settings
   - Manage categories
   - Set system parameters

---

## Project URLs

### Main URL Configuration (project2/urls.py)

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('examapp/', include('examapp.urls')),
]
```

### App URL Configuration (examapp/urls.py)

Expected URLs:

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('exams/', views.exam_list, name='exam_list'),
    path('exams/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('exams/<int:exam_id>/take/', views.take_exam, name='take_exam'),
    path('results/<int:exam_id>/', views.view_results, name='view_results'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
```

---

## Django Models & Database

### Model Relationships

```
User (Django built-in)
├── Exam (created_by)
├── StudentExam
│   ├── exam (ForeignKey)
│   └── student (ForeignKey)
└── StudentAnswer
    ├── student_exam (ForeignKey)
    ├── question (ForeignKey)
    └── selected_answer
```

### Database Tables Created

- `auth_user` - User accounts
- `examapp_exam` - Exam records
- `examapp_question` - Questions for exams
- `examapp_studentexam` - Student exam attempts
- `examapp_studentanswer` - Individual answers (if applicable)

### Create Initial Data

```bash
# Create superuser
python manage.py createsuperuser

# Create sample data (if you have a script)
python manage.py load_initial_data
```

---

## Static Files & CSS

### CSS Structure

Static files are located in `examapp/static/`:

```
examapp/static/
├── css/
│   └── style.css          # Main stylesheet
├── js/
│   └── script.js          # JavaScript functionality
└── images/
    ├── logo.png
    └── icons/
```

### Using Static Files in Templates

In HTML templates, load static files using Django template tags:

```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

### Collecting Static Files

```bash
# Collect all static files to STATIC_ROOT directory
python manage.py collectstatic
```

---

## Common Issues & Troubleshooting

### Issue 1: MySQL Connection Error

**Error**: `django.db.utils.OperationalError: (2003, "Can't connect to MySQL server")`

**Solutions**:
```bash
# Check if MySQL is running
# On Windows: Services → Check if MySQL is running
# On macOS: mysql.server status
# On Linux: sudo service mysql status

# Start MySQL if not running
mysql.server start  # macOS
sudo service mysql start  # Linux
```

Check `settings.py` database configuration:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '1276db',
        'USER': 'root',
        'PASSWORD': 'root123',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```

---

### Issue 2: ModuleNotFoundError: No module named 'django'

**Solution**:
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install Django
pip install Django==5.2.3
```

---

### Issue 3: Static Files Not Loading

**Error**: CSS/JS files return 404

**Solutions**:
```bash
# Collect static files
python manage.py collectstatic --noinput

# Check STATIC_URL in settings.py
STATIC_URL = '/static/'

# Verify static files folder exists
# examapp/static/ should contain css, js, images folders
```

In template, ensure using correct template tag:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

---

### Issue 4: Database Migrations Failed

**Solutions**:
```bash
# Show migration status
python manage.py showmigrations

# Reset migrations (caution: deletes data)
python manage.py migrate examapp zero

# Recreate migrations
python manage.py makemigrations
python manage.py migrate

# If still issues, try:
python manage.py migrate --run-syncdb
```

---

### Issue 5: Port Already in Use

**Error**: `Address already in use: ('127.0.0.1', 8000)`

**Solution**:
```bash
# Run on different port
python manage.py runserver 8001

# Or kill process using port 8000
# On Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# On macOS/Linux:
lsof -i :8000
kill -9 <PID>
```

---

### Issue 6: ImportError: No module named 'pymysql'

**Solution**:
```bash
# Install PyMySQL
pip install PyMySQL

# Ensure it's in requirements.txt and installed
pip install -r requirements.txt
```

---

## Contributing

We welcome contributions to improve the Exam System!

### How to Contribute

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/project2.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make changes** and test thoroughly
   ```bash
   python manage.py test
   ```

4. **Commit with clear messages**
   ```bash
   git commit -m "Add: description of your feature"
   ```

5. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request** with detailed description

### Coding Standards
- Follow PEP 8 style guide
- Write clear comments for complex logic
- Add docstrings to functions and classes
- Test all changes before committing

---

## License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

The MIT License allows:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

With the condition of:
- 📋 Include original license and copyright notice

---

## Contact & Support

### Author
**Deepak Rathod**
- GitHub: [@deepakrathod19](https://github.com/deepakrathod19)
- Email: deepak@example.com
- Repository: [project2](https://github.com/deepakrathod19/project2)

### Support Resources
- 📖 [Django Documentation](https://docs.djangoproject.com/)
- 🐛 [GitHub Issues](https://github.com/deepakrathod19/project2/issues)
- 💬 [Django Community Forum](https://forum.djangoproject.com/)

### Getting Help
1. Check [Troubleshooting](#common-issues--troubleshooting) section
2. Search existing GitHub issues
3. Create new issue with detailed information:
   - Error message and traceback
   - Steps to reproduce
   - System information (OS, Python version, Django version)
   - Screenshots if applicable

---

## Recommended Project Name

While "project2" works, consider renaming to one of these:

### Top 5 Recommendations
1. **ExamHub** - Modern, professional, clear purpose
2. **EduExam** - Education-focused, simple
3. **QuizPro** - Professional assessment tool
4. **TestMaster** - Comprehensive exam system
5. **OnlineExam** - Descriptive and clear

**To rename repository**:
1. Go to GitHub repository settings
2. Change name in "Repository name" field
3. GitHub automatically redirects old URLs

---

## Roadmap & Future Features

- [ ] Add mobile-responsive design improvements
- [ ] Implement exam result PDF export
- [ ] Add email notifications for exam schedules
- [ ] Create REST API endpoints
- [ ] Add question difficulty analytics
- [ ] Implement proctoring features
- [ ] Add multilingual support
- [ ] Create mobile app version
- [ ] Add advanced reporting and analytics

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | Nov 2025 | Initial release with exam management |
| - | - | More versions coming |

---

## Security Notes

⚠️ **Important**: Before deploying to production:

1. **Change DEBUG mode**:
   ```python
   DEBUG = False  # Set to False in production
   ```

2. **Update ALLOWED_HOSTS**:
   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

3. **Generate new SECRET_KEY**:
   ```python
   SECRET_KEY = 'your-new-secret-key-here'
   ```

4. **Use environment variables** for sensitive data:
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   SECRET_KEY = os.getenv('SECRET_KEY')
   DB_PASSWORD = os.getenv('DB_PASSWORD')
   ```

5. **Enable HTTPS** and set security headers

---

Made with myself by the development team | © 2025 All rights reserved.

**Last Updated**: November 2025  
**Django Version**: 5.2.3  
**Python Version**: 3.10+  
**Database**: MySQL 5.7+
