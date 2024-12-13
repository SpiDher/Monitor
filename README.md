---

Django Logger App

A simple Django application to log each HTTP request with a timestamp and request count. The logs are stored in a file (request_logs.log), and a JSON response is returned to the client.

Features

Logs each incoming request with:

Request count.

Current timestamp.


Stores logs in a file named request_logs.log.

Provides a JSON response with details of the request.


Requirements

Python 3.x

Django 3.x or later


Installation

1. Clone the repository or download the project files.


2. Navigate to the project directory:

cd myproject


3. Install the required dependencies:

pip install django


4. Run database migrations:

python manage.py migrate



Usage

1. Start the Django development server:

python manage.py runserver


2. Access the logging endpoint:

http://127.0.0.1:8000/logger/log/



Example Requests

cURL:

curl http://127.0.0.1:8000/logger/log/

Python:

import requests

response = requests.get('http://127.0.0.1:8000/logger/log/')
print(response.json())


Example Response

{
    "message": "Request logged successfully.",
    "request_count": 1,

