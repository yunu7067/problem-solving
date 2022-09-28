-- 코드를 입력하세요
SELECT
    i.animal_id as ANIMAL_ID,
    i.name as NAME
FROM animal_ins as i LEFT JOIN animal_outs as o ON i.animal_id = o.animal_id
WHERE o.datetime IS NOT NULL
ORDER BY (o.datetime - i.datetime) DESC
LIMIT 2