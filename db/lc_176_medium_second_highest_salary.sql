/*
176. Second Highest Salary
Medium
https://leetcode.com/problems/second-highest-salary/description/


SQL Schema
Pandas Schema

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

 
Write a solution to find the second highest distinct salary from the Employee table. 
If there is no second highest salary, return null (return None in Pandas).
The result format is in the following example.

 
Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+


*/


-- Solution 1: 2 MAX
SELECT MAX(salary) as SecondHighestSalary
FROM Employee 
WHERE NOT salary IN (
    SELECT MAX(salary) FROM Employee
)

-- Solution 2: use LIMIT and OFFSET
SELECT
(SELECT DISTINCT salary 
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1) AS SecondHighestSalary;
/* 
--  Returns no rows at all if the subquery returns no rows
SELECT salary AS SecondHighestSalary
FROM
(SELECT DISTINCT salary 
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1) AS SubqueryAlias;
*/
-- Note: the difference is the scalar subqueries returns NULL if there is no results.
-- Direct SELECT the scalar subqueries will result in a NULL if there is no result in subqueries
-- but if use SELECT <col> FROM <subquerie>, the the result is no row if there is no result in subqueries




-- Solution #3, CTE + ROW_NUM
WITH sorted_salary AS (
    SELECT DISTINCT salary, 
           DENSE_RANK() OVER (ORDER BY salary DESC) AS row_num
    FROM Employee
)
SELECT MAX(salary) AS SecondHighestSalary 
FROM sorted_salary
WHERE row_num = 2;
-- "ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num" will fail due to duplicate salary
-- DENSE_RANK() can fix that

/*
-- this isn't correct as the salary in COALESCE(salary, NULL) is a scalar value, the is no row when sorted_salary has no row
-- however 'aggrate functions' like MAX() return null when there is no row.
WITH sorted_salary AS (
    SELECT DISTINCT salary, 
           ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
    FROM Employee
)
SELECT COALESCE(salary, NULL) AS SecondHighestSalary 
FROM sorted_salary
WHERE row_num = 2;
*/


