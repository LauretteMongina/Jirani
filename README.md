# Jirani
Laurette Mong'ina 
  
# Description  
This is a Django neighbourhood  website application where a user must signup first, be able to join a hood and once you 
join a hood, see businesses and news in the neighbourhood you belong to.  
##  Live Link  
https://gramjirani.herokuapp.com/
  
 
## User Story  
  
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 bash 
https://github.com/LauretteMongina/Jirani.git

##### Navigate into the folder and install requirements  
 bash 
cd jirani

##### Install and activate Virtual  
 bash 
- python3 -m venv virtual - source virtual/bin/activate  
  
##### Install Dependencies  
 bash 
 pip install -r requirements.txt 
  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 bash 
python manage.py makemigrations hood
  
 Now Migrate  
 bash 
 python manage.py migrate 

##### Run the application  
 bash 
 python manage.py runserver 
 
##### Testing the application  
 bash 
 python manage.py test 

Open the application on your browser `127.0.0.1:8000`.  
  
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 2.2.6](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* Search function does not work.
  
## Contact Information   
If you have any question or contributions, please email me at [monginalaurette@gmail.com]  
  

* Copyright (c) 2021 Laurette