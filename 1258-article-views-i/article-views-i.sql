-- Write your PostgreSQL query statement below
SELECT DISTINCT a.author_id as id FROM Views a WHERE a.author_id = a.viewer_id;