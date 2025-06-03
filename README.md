Student Performance Tracking System
This is a Django-based web application for tracking student performance, including managing students, subjects, grades, and generating performance reports.
Prerequisites

Python 3.10+
Git
Virtualenv (optional but recommended)

Setup Instructions

Clone the repository:
git clone https://github.com/ArtemWasin/student-performance.git
cd student-performance


Create and activate a virtual environment (on your computer named nubik):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install django


Run migrations:
python manage.py migrate


Create user groups and default users:
python manage.py create_groups_and_users


Run the development server:
python manage.py runserver


Access the application:

Open http://127.0.0.1:8000/ in your browser.
Admin login: admin / admin123
Teacher login: teacher / teacher123
Student login: student / student123



Features

Admin: Full access to create/edit/delete students, subjects, and grades.
Teacher: View and assign grades to students.
Student: View their own grades.
Reports: A dedicated page showing the best and worst students, average grades by student, and by subject by clicking on the "Reports" link in the navigation bar.

Project Structure

student_performance/: Django project directory.
performance/: Django app for managing students, subjects, and grades.
templates/: HTML templates for the frontend.
static/: Static files (CSS, Bootstrap).

Git Commits
The project is versioned with the following commits:

Initial project setup and Git repository initialization.
Creation of models and migrations.
Implementation of views, URLs, and templates.
Addition of user groups, permissions, and reports.

