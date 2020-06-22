import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name   =   db.Column(db.String(), nullable=False)
    email       =   db.Column(db.String(), nullable=False)
    password    =   db.Column(db.String(), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)    

class Course(db.Model):
    __tablename__ = 'course'
    course_id   =   db.Column(db.Integer, primary_key=True)
    title       =   db.Column(db.String(), nullable=False)
    description =   db.Column(db.String(), nullable=False)
    credits     =   db.Column(db.Integer, nullable=False)
    term        =   db.Column(db.String(), nullable=False)
    link        =   db.Column(db.String(), nullable=False)

class Enrollment(db.Model):
    e_id   =   db.Column(db.Integer, primary_key=True)
    user_id     =  db.Column(db.Integer, nullable=False)
    course_id   =   db.Column(db.Integer, nullable=False)