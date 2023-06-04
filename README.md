# How To Run
## Virtualenv
***

> Language: python3
> 
> Framework: Flask
> 
> DB: MySQL 8.0.32

Virtual environment installation & configuration
``` bash
$ sudo pip3 install virtualenv
``` 

Create virtual environment in the project directory and activate it.
``` bash
$ virtualenv [venv_name] -p python3
$ source [venv_name]/bin/activate
``` 
If you want to deactivate the virtual environment, run the following command.
```bash
(venv)$ deactivate
```  
## How to start the project
***
1. DB Configuration
   1) Install the packages that defined in the "requirements.txt" file by the following command.
   ```
   (venv)$ pip install -U -r requirements.txt
   ```
   2) Insert db password in th keys.xml file. The "keys.xml" file must be in the same directory where the "app.py" file exists in.
   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <resources>
    <string name="DB_PWD">your_db_password</string>
   </resources>
   ```
   3) Run the following command sequentially.
   ```bash
   (venv)$ flask db init
   ```
   ```bash
   (venv)$ flask db migrate
   ```
   ```bash
   (venv)$ flask db upgrade
   ```
2. Run the flask server.
   ```bash
   (venv)$ flask run
   ```
   1) If you want to run the server in debugger mode, attach "--debug" option in the last.
   ```bash
   (venv)$ flask run --debug
   ```
   2) If you want to quit the server, click on the terminal and press 'CTRL+C'. 
3. DB Update Error
   1) Check the final head version.
      ```bash
      (venv)$ flask db heads
      ```
   2) Check the current version.
       ```bash
      (venv)$ flask db current
      ```
   3) Let current pointer point to the head.
      ```bash
      (venv)$ flask db stamp heads
      ```
   4) Recheck the current version.
      ```bash
      (venv)$ flask db current
      ```
   5) Run the following command sequentially to get the DB updated.
      ```bash
      (venv)$ flask db migrate
      ```
      ```bash
      (venv)$ flask db upgrade
      ```
## Packages
***
1. Flask-SQLAlchemy
``` bash
(venv)$ pip install flask-sqlalchemy
```
2. Flask-Migrate
```bash
(venv)$ pip install flask-migrate
```
3. Flask-Login
```bash
(venv)$ pip install flask-login
```
***
Write the required packages in the "requirements.txt" file to easily install the packages.
1. Install the required packages.
```bash
(venv)$ pip install -U -r requirements.txt
```
2. To write all the using packages in the "requirements.txt" automatically by running the following command.
```bash
(venv)$ pip freeze > requirements.txt
```