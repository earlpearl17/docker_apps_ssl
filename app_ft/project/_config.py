import os
import psycopg2

DEBUG = True
#DEBUG = False

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

#DATABASE = 'flasktaskr.db'
DATABASE = 'flasktaskrdb'
#USERNAME = 'admin'
#PASSWORD = 'admin'
#WTF_CSRF_ENABLED = True
CSRF_ENABLED = True
SECRET_KEY = 'myprecious'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# define the full path for the database
#DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{username}:{password}@localhost:{port}/foodversity_db".format(username=pg_user, password=pg_pwd, port=pg_port)
#SQLALCHEMY_DATABASE_URI = "postgresql://taskruser:flask1234@localhost:5432/flasktaskrdb"
#SQLALCHEMY_DATABASE_URI = "postgresql://taskruser:flask1234@db:5432/flasktaskrdb"
#SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://taskruser:flask1234@db:5432/flasktaskrdb"
#SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/flasktaskrdb"
#SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@db:5432/flasktaskrdb"
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://taskruser:flask1234@db:5432/flasktaskrdb"


