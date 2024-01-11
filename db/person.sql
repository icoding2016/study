create database person_db;
show databases;
use person_db;
CREATE TABLE person (
  id INTEGER,
  name varchar(64) NOT NULL,
  info TEXT NOT NULL
);
CREATE TABLE skills (
  id INTEGER PRIMARY KEY,
  name varchar(64) NOT NULL
);
CREATE TABLE person_skills (
  pid INTEGER,
  sid INTEGER
);
show tables;
# insert data to tables
INSERT INTO person VALUES (0001, 'Clark', 'Clark the Sales and musician');
INSERT INTO person VALUES (0002, 'Dave', 'Dave the Accounting and doctor');
INSERT INTO person VALUES (0003, 'Ava', 'Ava the Sales');
INSERT INTO person VALUES (0004, 'Jerry', 'Jerry the engineer and doctor');

INSERT INTO skills VALUES (1001, 'Sales');
INSERT INTO skills VALUES (1002, 'Accounting');
INSERT INTO skills VALUES (1003, 'Musician');
INSERT INTO skills VALUES (1004, 'Engineer');
INSERT INTO skills VALUES (1005, 'Doctor');

INSERT INTO person_skills VALUES (0001, 1001);
INSERT INTO person_skills VALUES (0001, 1003);
INSERT INTO person_skills VALUES (0002, 1002);
INSERT INTO person_skills VALUES (0002, 1005);
INSERT INTO person_skills VALUES (0003, 1001);
INSERT INTO person_skills VALUES (0004, 1004);
INSERT INTO person_skills VALUES (0004, 1005);

select * from person;
select * from skills;
select * from person_skills;
# select person by certain skill.
select person.name, skills.name from person join person_skills on person_skills.pid=person.id join skills on skills.name='Sales' and skills.id=person_skills.sid;
# show a person's skills
select person.name, skills.name from skills join person_skills on skills.id=person_skills.sid join person on person.id=person_skills.pid and person.name="Jerry";
