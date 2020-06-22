Learning Hub
-----
### Introduction
This project is online portal web-application for students where there are different features available like Login, Registration, Enroll Course, check My Course and learn new technology.

### Overview

you should have a fully functioning site that is at least capable of doing the following, if not more, using a PostgreSQL database:

* Regitraion & Login.
* Enroll Course.
* Start Learning.

### Tech Stack

Our tech stack will include:

* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations
* **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for our website's frontend

 ```sh
  ├── README.md
  ├── courses.py *** Before run main.py run this script
  ├── app.py *** the main driver of the app."flask run" to run after installing dependences
  ├──application
      ├── __init__.py "application setup"
      ├── forms.py, models.py, routes.py
      ├── static
      │   ├── css
      │   ├── images
      └── templates
  ├──config.py "connect database"
  ├──requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ```
### Setup
1. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```
2. setup your database in config.py:
  ```
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/databaseName'  

  ```
  in config.py file.
  For Database create at PostgreSQL
  ```
  postgres-# CREATE DATABASE learninghub;
  ```
  You can check the available database list using \l
  ```
  postgres-# \l
  ```
  command to connect/select a desired database
  ```
  postgres=# \c learninghub;
  ```

3. Run the development server:

  ```
  Create Migration 
    $  flask db init

  You can then generate an initial migration
    $ flask db migrate -m "Initial migration."

  Then you can apply the migration to the database:
    $ flask db upgrade
  ```
4. insert data into Course table.
    ```
    $ python courses.py 
    
    ```
    for Default Courses.

5. Run Application:
  ```
  $ flask run
  ```
  Open Browser > http://127.0.0.1:5000/


# Deployment In Heroku
Important "Procfile" file
#### Steps
1. create account
   https://id.heroku.com/login 

2. create application in heroku 

4. Create database and click copy connection link and paste inside app.py for database connectivity

3. Upload project in github 

4. In heroku click on deployment inside application and select option  deploy with github then connect repo and deploy 

5. Use commandline interface of heroku for migration and run courses.py for default courses

6. finally Application will deploy click on URL and open application.

### User Interface

![Home page](https://github.com/imshubh17/Projects/blob/master/images/New%20folder/home.PNG?raw=true "Home")

![Home page](https://github.com/imshubh17/Projects/blob/master/images/New%20folder/courses.PNG?raw=true "Courses")

![Home page](https://github.com/imshubh17/Projects/blob/master/images/New%20folder/MyCourse.PNG?raw=true "My course")

![Home page](https://github.com/imshubh17/Projects/blob/master/images/New%20folder/login.PNG?raw=true "Login Page")

![Home page](https://github.com/imshubh17/Projects/blob/master/images/New%20folder/register.PNG?raw=true "Registration Page")

