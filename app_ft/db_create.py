# project / db_create.py

from datetime import date

from project import db
from project.models import Task, User

#import pdb

#pdb.set_trace()

# create the database and the db table
db.create_all()

# insert data
db.session.add(
    User("admin", "ad@min.com", "$2b$12$6YdHGWpB9YRzTKhBkQqxX.10CmbmVPq9a9G1.P9v2PZRxRy51Tt8y", "admin")
)

db.session.add(
    Task("Migrate to PostgreSQL DB", date(2020, 8, 13), 10, date(2020, 8, 12), 1, 1)
)

db.session.add(
    Task("Finish Real Python Part 2", date(2020, 9, 17), 10, date(2020, 8, 7), 1, 1)
)

# commit the changes
db.session.commit()
