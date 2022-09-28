-- 코드를 입력하세요

SELECT i.name as 'NAME', i.datetime as 'DATETIME'
FROM animal_ins as i LEFT JOIN animal_outs as o ON i.animal_id = o.animal_id
WHERE o.datetime IS NULL
ORDER BY i.datetime
LIMIT 3
