from application import db
from application.models import Course


c1 = Course(course_id = 1111, title = 'Learn Python', description = 'Basic understading of Python programming', credits=8, term='programming',link="https://www.python.org/doc/")
c2 = Course(course_id = 5697, title = 'Learn Go', description = 'Basic understading of go programming', credits=8, term='programming',link="https://golang.org/doc/")
c3 = Course(course_id = 1542, title = 'Learn Flask', description = 'Basic understading of go framework', credits=8, term='framework',link="https://flask.palletsprojects.com/en/1.1.x/quickstart/")
c4 = Course(course_id = 8963, title = 'Learn Posgresql', description = 'Basic Queres of psql database', credits=8, term='database',link="https://www.tutorialspoint.com/postgresql/index.htm")
db.session.add(c1)
db.session.add(c2)
db.session.add(c3)
db.session.add(c4)
db.session.commit()
    
