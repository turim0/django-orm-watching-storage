# Django ORM watching storage

This project interacts with SQL database that contains nessesary information to control visits in bank storage and 
displays this information on the website.

# Quickstart

Сreate `.env` file and add parametrs:   
```  
DATABASE_URL=postgresql://user:password@host:port/database
DEBUG=False   
SECRET_KEY=secret_key
```
Availble enviroment params your can take from [documetation](https://docs.djangoproject.com/en/3.0/ref/settings/)

Example of script launch on Linux, Python 3.6:

```bash
$ pip install -r requirements.txt
$ python manage.py runserver 0.0.0.0:8000
```
#Project Goals
The code is written for educational purposes - this is a lesson in the course on Python and web development on the site Devman.