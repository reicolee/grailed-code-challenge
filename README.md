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

# Install project depedencies
pip install -Ur requirements.txt

# Start the local development server
python manage.py runserver

# Running the tests
pytest

```

## Navigate to the designated URL to view results

```
GET

POST
```

## Discussion

### Technologies

Django:
I have been using Django for 1.5 years.

Django REST Framework:

### Design & Tradeoffs
