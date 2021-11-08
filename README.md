# Django-REST-Demo

This is a sample project created to demonstrate Django Rest Framework,

To know more about problem statement for this assignment, [click here](docs/problem_statement.md)

---

## How to run this project

1. Install python (above 3.7) on your machine
2. In root folder of this project, create a virtual environment. You can find more about virtual environment [here](https://docs.python.org/3/tutorial/venv.html)
3. Once Virtual environment is created, Activate it.
4. Run following command to install all dependent packages -
   ```
   pip install -r requirements.txt
   ```
5. Go to src folder and run following command to create database tables -
   ```
   python manage.py migrate
   ```
6. Next you have to create a superuser to access protected APIs. Run following command to create a superuser
   ```
   python manage.py createsuperuser
   ```
   Fill in details and complete superuser creation process.
7. Run following command to run the project
   ```
   python manage.py runserver
   ```
8. Access admin panel at http://127.0.0.1:8000/admin, login and add some data in all models (except groups)
9. If you visit http://127.0.0.1:8000/, Page will be redirected to swagger which is what we use to document our APIs and share with frontend users or consumers. You need add credentials by clicking on Authorize to access protected APIs. I have actually allowed Basic, Session and JWT authentication in this project.

---

## What you must avoid from this project

1. Never store your private values such as SECRECT_KEY, Database creedentials or any other secret tokens or API keys etc directly in settings.py as it is demo project I have stored

**Note:** If you want to add more points, You are always welcome to contribute. Thanks!
