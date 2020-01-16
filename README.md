# Django ORM watching storage

This project interacts with SQL database that contains nessesary information to control visits in bank storage and 
displays this information on the website.

# Quickstart

Сreate .env file and add parametrs according to your databasegit:   
HOST=host   
PORT=port  
NAME=name  
USER=user   
PASSWORD=password   
SECRET_KEY=secret_key

Example of script launch on Linux, Python 3.6:

```bash
~$pip install -r requirements.txt
~$python main.py
```


Server starts at http://0.0.0.0:8000/