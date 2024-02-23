-- Schema
DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id           serial PRIMARY KEY,
  first_name   varchar(255) NOT NULL,
  last_name    varchar(255) NOT NULL,
  age           integer,
  subject       integer
);

COPY students FROM '/Users/hank/code/whiskey/week4/23FEB_Flask_Intro/flask_postgres_school/data/student.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
  id           serial PRIMARY KEY,
  first_name   varchar(255) NOT NULL,
  last_name    varchar(255) NOT NULL,
  age           integer,
  subject       integer
);

COPY teachers FROM '/Users/hank/code/whiskey/week4/23FEB_Flask_Intro/flask_postgres_school/data/teachers.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects ( 
  id serial PRIMARY KEY, 
  subject varchar(255)
);

COPY subjects FROM '/Users/hank/code/whiskey/week4/23FEB_Flask_Intro/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;

