# Setup 
pip install django
django-admin startproject <projectName>
python manage.py startapp <appName>
python manage.py runserver

Install "django" extension on VSCode


# Run
python manage.py runserver
go to http://localhost:8000/
admin console: http://localhost:8000/admin 


# Model change
python manage.py makemigrations (add table to sqlite3)
python manage.py migrate (update the app)


# Admin panel
python manage.py createsuperuser (create admin user)
http://localhost:8000/admin


# CORS origin
To allow react to send http request to django localhost
pip install django-cors-headers


# Doubts
Project vs App: A project can include multiple apps, each serving a specific functionality of the web application.