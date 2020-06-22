from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for,session
from application.forms import LoginForm, RegisterForm
from application.models import User, Course, Enrollment

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True )

@app.route("/login", methods=['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data

        user = User.query.filter_by(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True )

@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('username',None)
    return redirect(url_for('index'))


@app.route("/courses")
def courses():
    lists=Course.query.all()
    return render_template("courses.html", courseData=lists, courses = True )

@app.route("/mycourse", methods=["GET","POST"])
def mycourse():
    if not session.get('username'):
        return redirect(url_for('login'))

    courseID = request.form.get('courseID')
    courseTitle = request.form.get('title')
    user_id = session.get('user_id')    
    if courseID:
        if Enrollment.query.filter_by(user_id=user_id,course_id=courseID).first():
            flash(f"Oops! You are already registered in this course {courseTitle}!", "danger")
            return redirect(url_for("courses"))
        else:
            enroll = Enrollment(user_id=user_id,course_id=courseID)
            db.session.add(enroll)
            db.session.commit()
            flash(f"You are enrolled in {courseTitle}!", "success")

    ec = Enrollment.query.filter_by(user_id=user_id).all()
    
    courses = [ Course.query.filter_by(course_id=i.course_id).first() for i in ec]    

    return render_template("mycourse.html", mycourse=True, data=courses)

@app.route("/register", methods=['POST','GET'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        user_id = User.query.count()
        user_id += 1
        user.user_id     = user_id
        user.email       = form.email.data
        user.password    = form.password.data
        user.first_name  = form.first_name.data
        user.last_name   = form.last_name.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You are successfully registered!","success")
        return redirect(url_for('index'))
    return render_template("registration.html", title="Register", form=form, registration=True)
