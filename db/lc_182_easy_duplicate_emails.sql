/*
182. Duplicate Emails
Easy
https://leetcode.com/problems/duplicate-emails/

SQL Schema
Pandas Schema

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.

 

Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output: 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.


*/

--------- Prepare ---------

CREATE DATABASE IF NOT EXISTS LC;
USE LC;

DROP TABLE Person;
CREATE TABLE IF NOT EXISTS Person (
  id  int,
  name  varchar(64),
  email varchar(64)
);

INSERT INTO Person VALUES (1, 'Joe', 'Joe@gmail.com');
INSERT INTO Person VALUES (2, 'Peter', 'Peter@yahoo.com');
INSERT INTO Person VALUES (3, 'Philip', 'Phil@msn.com');
INSERT INTO Person VALUES (4, 'Peter Parker', 'Peter@yahoo.com');


SELECT * FROM Person;

-------------------------------------------

SELECT email 
FROM Person
GROUP BY email
HAVING COUNT(email) > 1
;
