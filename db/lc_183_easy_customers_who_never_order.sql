/*
183. Customers Who Never Order
Easy
https://leetcode.com/problems/customers-who-never-order/

SQL Schema
Pandas Schema

Table: Customers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.

 

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

 

Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+


*/

--------- Prepare ---------

CREATE DATABASE IF NOT EXISTS LC;
USE LC;

CREATE TABLE IF NOT EXISTS Customers (
  id  int,
  name  varchar(64)
);
CREATE TABLE IF NOT EXISTS Orders (
  id int,
  customerId int
);

INSERT INTO Customers VALUES (1, 'Joe');
INSERT INTO Customers VALUES (2, 'Henry');
INSERT INTO Customers VALUES (3, 'Sam');
INSERT INTO Customers VALUES (4, 'Max');
INSERT INTO Orders VALUES (1, 3);
INSERT INTO Orders VALUES (2, 1);

SELECT * FROM Customers;
SELECT * FROM Orders;

-------------------------------------------

SELECT c.name as Customers
FROM Customers as c
LEFT JOIN Orders as o
ON o.customerId=c.id
GROUP BY Customers
HAVING COUNT(o.customerId)=0
;