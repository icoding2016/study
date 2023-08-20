/*
Leetcode SQL
1454. Active Users

Table Accounts:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
the id is the primary key for this table.
This table contains the account id and the user name of each account.

Table Logins:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| login_date    | date    |
+---------------+---------+
There is no primary key for this table, it may contain duplicates.
This table contains the account id of the user who logged in and the login date. A user may log in multiple times in the day.

Write an SQL query to find the id and the name of active users.
Active users are those who logged in to their accounts for 5 or more consecutive days.
Return the result table ordered by the id.

The query result format is in the following example:

Accounts table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Winston  |
| 7  | Jonathan |
+----+----------+Logins table:
+----+------------+
| id | login_date |
+----+------------+
| 7  | 2020-05-30 |
| 1  | 2020-05-30 |
| 7  | 2020-05-31 |
| 7  | 2020-06-01 |
| 7  | 2020-06-02 |
| 7  | 2020-06-02 |
| 7  | 2020-06-03 |
| 1  | 2020-06-07 |
| 7  | 2020-06-10 |
+----+------------+Result table:
+----+----------+
| id | name     |
+----+----------+
| 7  | Jonathan |
+----+----------+
User Winston with id = 1 logged in 2 times only in 2 different days, so, Winston is not an active user.
User Jonathan with id = 7 logged in 7 times in 6 different days, five of them were consecutive days, so, Jonathan is an active user.

Follow up question:
Can you write a general solution if the active users are those who logged in to their accounts for n or more consecutive days?

*/

# prepare data
CREATE database user_login;
USE user_login;
CREATE table accounts (id INT, name varchar(64), primary key (id));
CREATE table logins (id INT, login_date date);
INSERT INTO accounts values (1, "Winston");
INSERT INTO accounts values (7, "Jonathan");
INSERT INTO logins values (7, "2020-05-30");
INSERT INTO logins values (1, "2020-05-30");
INSERT INTO logins values (7, "2020-05-31");
INSERT INTO logins values (7, "2020-06-01");
INSERT INTO logins values (7, "2020-06-02");
INSERT INTO logins values (7, "2020-06-03");
INSERT INTO logins values (1, "2020-06-07");
INSERT INTO logins values (7, "2020-06-10");
SHOW TABLES;
SELECT * from accounts;
SELECT * from logins;

# COUNT
SELECT distinct id, login_date, count(login_date) over (partition by id order by id) as count from logins;
# LAG
SELECT distinct id, login_date, LAG(login_date, 1) OVER (partition by id order by id) as last_login FROM logins;


SELECT distinct id, login_date, LAG(login_date, 4) OVER (partition by id order by id) as lag_4 FROM logins;

# Find Active Users (continues login 5 days)
WITH 
Lag4 AS (
  SELECT distinct id, login_date,
    LAG(login_date, 4) OVER (partition by id order by id) as lag_4 
  FROM logins
),
ActiveUsers AS (
  SELECT id, login_date, lag_4 FROM Lag4
  WHERE login_date - lag_4 >= 4
)
SELECT distinct au.id, acc.name 
FROM ActiveUsers as au 
JOIN accounts as acc ON au.id=acc.id;



-- CREATE FUNCTION xxx
-- ( @id AS INT ) 
-- RETURN INT
-- AS
-- BEGIN
--   SELECT id, name FROM accounts
-- END 



