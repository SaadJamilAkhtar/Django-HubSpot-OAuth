# HubSpot OAuth with Django
## Description:
The purpose of the project is to implement HubSpot OAuth with django application.

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
5. Create a HubSpot app
6. Visit django admin at "\admin"
7. log in to admin 
8. In HubSpot Credentials model create a new entry with client id, client secret and redirect url (as recorded in registered app)
9. visit application main page while user is logged in.
10. follow steps and add HubSpot credentials.
11. a new entry in Hub spot tokens model will be created with access token and refresh token.
12. access_token and refresh tokens can be used in further requests to HubSpot api.

### Note:
For this example only oauth permission was added to HubSpot app if you want to change permissions change url in auth() in HubSpot -> views.py file

# Resources
For details on HubSpot OAuth visit [Link](https://developers.hubspot.com/docs/api/working-with-oauth)