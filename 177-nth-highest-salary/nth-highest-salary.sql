CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN

   IF N <= 0 THEN
        RETURN;
   END IF;

  RETURN QUERY (
    SELECT (
      SELECT DISTINCT p.salary 
      FROM Employee p
      ORDER BY p.salary DESC 
      OFFSET GREATEST(N - 1) 
      LIMIT 1
    )
  );
END;
$$ LANGUAGE plpgsql;