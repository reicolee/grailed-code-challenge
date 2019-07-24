# Grailed Backend Coding Exercise

## Requirements

- Create a function to finds all users with disallowed usernames.
- Create a function to resolve all username collisions, with an optinal 'dry run argument' that will print the affected rows without updating the databsae.
- Create a fuction to resolve all disallowed usernames, with an optinal 'dry run argument' that will print the affected rows without updating the database.

## Installation

Python 3 and pip3 are required in your local machine in order to run the Django development server. To install Python 3, you can follow the instructions [here](https://www.python.org/downloads/?source=post_page---------------------------) in the Python Software Foundations page. pip3 are included when Python 3 gets installed.

```python
# In your terminal, perform the follwing commands to install dependencies needed to run the project

# Check to make sure Python 3 is installed
python3 --version

# Check to make sure pip3 is installed
pip3 --version

# Install virtualenv
pip3 install virtualenv

# Clone the repository
git@github.com:reicolee/grailed-code-challenge.git

# Create a virtualenv
virtualenv -p python3 venv

# Activate the virtualenv
source venv/bin/activate

# Install project depedencies, such as Django and Django REST
pip install -Ur requirements.txt

# Start the development server
python manage.py runserver

# To exit virtualenv
deactivate

```

## API Guide

Once the development server is up and running, navigate to one of the following web-browsable APIs to view:

List of users with disallowed usernames:

GET: [localhost:8000/users/disallowed_users/](localhost:8000/users/disallowed_users/)

List of users with updated usernames from previously disallowed usernames. To update aka POST, scroll to the bottom, and hit the 'POST' button underneath the form:

POST: [localhost:8000/users/disallowed_users/](localhost:8000/users/disallowed_users/)

List of users with duplicate usernames:

GET: [localhost:8000/users/duplicate_users/](localhost:8000/users/duplicate_users/)

List of users with updated usernames from previously duplicate usernames. To update aka POST, scroll to the bottom, and hit the 'POST' button underneath the form:

POST: [localhost:8000/users/duplicate_users/](localhost:8000/users/duplicate_users/)

## Discussion

### API Explanation

Django provides core scaffolding for the application out of the box, where most of the boilerplate code lives within the `./config` folder (created by running the command `django-admin startproject config .`), taking care of the configurations of the application. Code written by me lives within the `./users` folder (created by running the command `python manage.py startapp users`).

#### `UsernamesResolutionHelper`

The main logic lives within `UsernamesResolutionHelper` helper class in the `./users/helpers.py` file.

### Technologies

Django:

- Familiarity: I have been using Django for roughly 1.5 - 2 years for both work and personal projects.
- ORM: Django includes a powerful ORM that supports a number of relational database out-of-the-box --SQLite, PostgreSQL, etc., which suits well with our use case for this project using SQLite3.
- Database queries:

Django REST Framework:

- Browsability:
-

```

```
