/*
177. Nth Highest Salary
Medium
https://leetcode.com/problems/nth-highest-salary/description/


Pandas Schema
data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})

SQL Schema
Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

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
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+



*/


-- Solution: ORDER + OFFSET
CREATE FUNCTION getNthHighestSalary(N INT) 
RETURNS INT
BEGIN
    DECLARE X INT;
    SET X = N - 1;
    RETURN (
        SELECT MAX(salary) as getNthHighestSalary
        FROM (
            SELECT DISTINCT salary
            FROM Employee
            ORDER BY salary DESC
            LIMIT 1 OFFSET X
        ) AS sorted_salary
    );
END



/*

Pandas solution:

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    se = employee.drop_duplicates(subset=['salary'])
    se = se.sort_values(by='salary', ascending=False).reset_index(drop=True)
    if len(se) < N or N < 1:
        return pd.DataFrame([{f'getNthHighestSalary({N})':pd.NA}])
    else:
        return pd.DataFrame([{f'getNthHighestSalary({N})': se.loc[N-1, 'salary']}])

# Note:
# Reset Index: After sorting, reset the index to ensure the row indices are consecutive integers, which makes it safe to use .loc with an integer index.

*/