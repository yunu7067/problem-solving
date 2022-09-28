-- 코드를 입력하세요
WITH RECURSIVE h AS (
    SELECT 0 AS `HOUR`
    UNION ALL
    SELECT HOUR + 1 FROM h WHERE HOUR < 23
) 


SELECT h.hour as `HOUR`, IFNULL(c.count, 0) as `COUNT`
FROM
    h LEFT JOIN
    (SELECT HOUR(o.datetime) as `HOUR`, COUNT(*) as `COUNT` FROM animal_outs AS o GROUP BY HOUR(o.datetime)) AS c 
    ON (h.hour = c.hour)
