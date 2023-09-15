/*
175. Combine Two Tables
Easy
https://leetcode.com/problems/combine-two-tables/

SQL Schema

Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key (column with unique values) for this table.
This table contains information about the ID of some persons and their first and last names.

Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key (column with unique values) for this table.
Each row of this table contains information about the city and state of one person with ID = PersonId.

Write a solution to report the first name, last name, city, and state of each person in the Person table. 
If the address of a personId is not present in the Address table, report null instead.
Return the result table in any order.

The result format is in the following example.

Example 1:

Input: 
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
Output: 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
Explanation: 
There is no address in the address table for the personId = 1 so we return null in their city and state.
addressId = 1 contains information about the address of personId = 2.



*/

--------- Prepare ---------

CREATE DATABASE IF NOT EXISTS LC;
USE LC;

CREATE TABLE IF NOT EXISTS Person (
  personId  int,
  lastName  varchar(64),
  firstName varchar(64)
);
CREATE TABLE IF NOT EXISTS Address (
  addressId int,
  personId  int,
  city  varchar(64),
  state varchar(64)
);

INSERT INTO Person VALUES (1, 'Wang', 'Allen');
INSERT INTO Person VALUES (1, 'Alice', 'Bob');
INSERT INTO Address VALUES (1, 2, 'New York City', 'New York');
INSERT INTO Address VALUES (1, 3, 'Leetcode', 'California');
SELECT * FROM Person;
SELECT * FROM Address;

-------------------------------------------

# using IFNULL
SELECT
  p.firstName AS firstName,
  p.lastName AS lastName,
  IFNULL(a.city, NULL) AS city,
  IFNULL(a.state, NULL) AS state
FROM Person AS p
LEFT JOIN Address AS a ON p.personId=a.personId;


# using COALESCE
SELECT
  p.firstName AS firstName,
  p.lastName AS lastName,
  COALESCE(a.city, NULL) AS city,
  COALESCE(a.state, NULL) AS state
FROM Person AS p
LEFT JOIN Address AS a ON p.personId=a.personId;