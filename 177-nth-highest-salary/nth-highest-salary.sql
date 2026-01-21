CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    SELECT (
      SELECT DISTINCT p.salary 
      FROM Employee p
      ORDER BY p.salary DESC 
      -- Usamos OFFSET con un valor que nunca sea menor a 0
      OFFSET GREATEST(N - 1, 0) 
      LIMIT 1
    )
    -- El WHERE filtra si N es válido antes de que la consulta externa devuelva algo
    WHERE N > 0
  );
END;
$$ LANGUAGE plpgsql;