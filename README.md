# Grailed Backend Coding Exercise

## Requirements

- Create a function to finds all users with disallowed usernames.
- Create a function to resolve all username collisions, with an optinal 'dry run argument' that will print the affected rows without updating the databsae.
- Create a fuction to resolve all disallowed usernames, with an optinal 'dry run argument' that will print the affected rows without updating the database.

## Installation

In order for this project to run, python3 and pip3 are required in your local machine.

```python

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

# Start the local development server
python manage.py runserver

```

## API Guide

Once the local development server is up and running, navigate one of the following web-browsable API to view:

List of users with disallowed usernames:

GET: [localhost:8000/users/disallowed_users/]

List of users with updated usernames from previously disallowed usernames. To update aka POST, scroll to the bottom, and hit the 'POST' button underneath the form:

POST: [localhost:8000/users/disallowed_users/]

List of users with duplicate usernames:

GET: [localhost:8000/users/duplicate_users/]

List of users with updated usernames from previously duplicate usernames. To update aka POST, scroll to the bottom, and hit the 'POST' button underneath the form:

POST: [localhost:8000/users/duplicate_users/]

## Discussion

### Technologies

Django:
I have been using Django for 1.5 years.

Django REST Framework:

### Design & Tradeoffs

```

```
