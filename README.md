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

## To run the test cases

```python
python manage.py test users
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

## API Explanation

I have been using Django for roughly 1.5 - 2 years for both work and personal projects.

Django provides core scaffolding for the application out of the box, where most of the boilerplate code lives within the `./config` folder (created by running the command `django-admin startproject config .`), taking care of the configurations of the application. Code written by me lives within the `./users` folder (created by running the command `python manage.py startapp users`).

The reason why I chose to present the data in the form of API endpoints instead of using a CLI application is because it seems intuitive for me to use a GET action for retrieving a list of users with either disallowed / duplicate usernames, and a POST action for updating the usernames to resolve collisions. Furthermore, instead of having to manually trigger certain functions to retrieve/view/update the data on the command line, having web browsable APIs to view the data is much more developer-friendly to inspect large amount of data.

The flow of the application are as follow:

When the request first comes in, it will check and go through the urls in `config/urls.py` and `users/urls.py`. Once Django finds a url that matches, it will invoke the view that is mapped to the url, in this case, either `duplicate_users` or `disallowed_users` in `users/views.py`.

### `UsernamesResolutionHelper`

The main logic for handling retrieving / updating users with disallowed / duplicate usernames lives within `UsernamesResolutionHelper` helper class in the `./users/helpers.py` file.

**Arguments: `resolve_type` and `dry_run`**

It accepts two arguments, `resolve_type` and `dry_run`. The `resolve_type` argument describes the type of users we would like to retrieve / resolve, the argument can be either 'duplicates' or 'disallowed', default to 'duplicates'. The `dry_run` arguments determines whether to return or update affected rows, default to `True` to prevent data from accidentally being updated.

**Instance Variable: `disallowed_usernames_list`**

Upon the instantiation of the `UsernamesResolutionHelper` class, it immediately queries the `disallowed_usernames` table and sets the instance variable `disallowed_usernames_list` as a list of disallowed usernames. This is due to the fact that both the queries for retrieving users with duplicate usernames and disallowed usernames need the list of disallowed usernamers for filtering.

Note: `get_disallowed_usernames_list` is a model class method that lives in `users/models.py` for querying disallowed usernames and returning them as a list.

**Instance Variable: `user_queries`**

Depending on the `resolve_type` argument, it will select corresponding methods to retrieve user queries.

**Class method: `update_users`**

**Class method: `get_users`**
