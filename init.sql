CREATE DATABASE portfoliodb;
CREATE DATABASE wordcounterdb;
CREATE DATABASE addressbookdb;
CREATE DATABASE learninglogdb;
CREATE DATABASE producthuntdb;
CREATE DATABASE blogdb;
CREATE DATABASE flasktaskrdb;
CREATE USER taskruser WITH PASSWORD 'flask1234'; 
CREATE USER bloguser WITH PASSWORD 'flask1234'; 
CREATE USER djangouser WITH PASSWORD 'pass1234'; 
GRANT ALL PRIVILEGES ON DATABASE portfoliodb TO djangouser; 
GRANT ALL PRIVILEGES ON DATABASE wordcounterdb TO djangouser;
GRANT ALL PRIVILEGES ON DATABASE addressbookdb TO djangouser;
GRANT ALL PRIVILEGES ON DATABASE learninglogdb TO djangouser;
GRANT ALL PRIVILEGES ON DATABASE producthuntdb TO djangouser;
GRANT ALL PRIVILEGES ON DATABASE blogdb TO bloguser;
GRANT ALL PRIVILEGES ON DATABASE flasktaskrdb TO taskruser;
\c blogdb bloguser;
CREATE TABLE posts (
	title VARCHAR (50) NOT NULL,
	post VARCHAR (300) NOT NULL
);

