/*
196. Delete Duplicate Emails
Easy
https://leetcode.com/problems/delete-duplicate-emails/

SQL Schema

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.

 

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

For Pandas users, please note that you are supposed to modify Person in place.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

The result format is in the following example.

 

Example 1:

Input: 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output: 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.

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

DELETE p1 FROM Person p1
JOIN Person p2
WHERE 
  p1.email=p2.email AND
  p1.id > p2.id
;

