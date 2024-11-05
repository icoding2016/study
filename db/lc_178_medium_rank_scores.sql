/*
178. Rank Scores
Medium
https://leetcode.com/problems/rank-scores/description/

SQL Schema
Pandas Schema

Table: Scores

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the score of a game. Score is a floating point value with two decimal places.

 

Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

    The scores should be ranked from the highest to the lowest.
    If there is a tie between two scores, both should have the same ranking.
    After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.

Return the result table ordered by score in descending order.

The result format is in the following example.

 

Example 1:

Input: 
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
Output: 
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+



*/

WITH ranked_scores AS (
    SELECT score,
           DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'    -- rank is reserved in MySQL, so use 'rank'
    FROM (
        SELECT DISTINCT score FROM Scores 
        -- ORDER BY score DESC
    ) AS dist_scores
)
SELECT s1.score, s2.rank
FROM Scores s1
INNER JOIN ranked_scores s2 ON s1.score=s2.score
ORDER BY score DESC


/*
# Panda solution

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    score_rank = scores.drop_duplicates(subset=['score']).sort_values(by='score', ascending=False)
    score_rank['rank'] = score_rank['score'].rank(method='dense', ascending=False).astype(int)
    sorted_score = scores.sort_values(by='score', ascending=False)
    merged = pd.merge(sorted_score[['score']], score_rank[['score', 'rank']])
    return merged

*/