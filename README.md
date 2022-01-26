# HubSpot OAuth with Django
## Description:
The purpose of the project is to implement Mailchimp OAuth with django application.

## Pre reqs:
1. Python
2. pip

## How to run application:
1. install required packages using requirements.txt  
`pip install -r requirements.txt`
2. migrate models to database using  
`python manage.py migrate` or  
`python3 manage.py migrate` (in case you have multiple versions of python installed)
3. add superuser using  
`python manage.py createsuperuser` or  
`python3 manage.py createsuperuser` (in case you have multiple versions of python installed)
4. run application using command  
`python manage.py runserver` or  
`python3 manage.py runserver` (in case you have multiple versions of python installed)


# Resources
For details on HubSpot OAuth visit [Link](https://developers.hubspot.com/docs/api/working-with-oauth)